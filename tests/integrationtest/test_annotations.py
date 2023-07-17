import os

from unittest import TestCase

from grafana_api.model import (
    APIModel,
    AnnotationObject,
    AnnotationGraphiteObject,
    FindAnnotationObject,
)
from grafana_api.annotations import Annotations


class AnnotationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    annotations: Annotations = Annotations(model)

    def test_a_find_annotations(self):
        self.assertEqual(
            140,
            self.find_annotation_by_text(
                "Test {alertname=Test, grafana_folder=Github Integrationtest} - Normal"
            ),
        )

    def test_b_create_annotation(self):
        annotations: AnnotationObject = AnnotationObject(
            dashboard_uid="tests",
            time=1000,
            time_end=10000,
            tags=["test"],
            text="test1",
        )

        annotation_id: int = self.annotations.create_annotation(annotations)

        self.assertEqual(
            "tests", self.find_annotation_by_id(annotation_id, "dashboardUID")
        )

    def test_c_create_graphite_annotation(self):
        annotations: AnnotationGraphiteObject = AnnotationGraphiteObject(
            what="test1", tags=["test1"], when=1000, data="test1"
        )
        self.assertIsNotNone(self.annotations.create_graphite_annotation(annotations))

    def test_d_update_annotation(self):
        annotations: AnnotationObject = AnnotationObject(
            text="test12", time_end=None, time=None, tags=None
        )

        annotation_id: int = self.find_annotation_by_text("test1")

        self.assertIsNone(
            self.annotations.update_annotation(annotation_id, annotations)
        )

        self.assertEqual("test12", self.find_annotation_by_id(annotation_id, "text"))

    def test_e_delete_annotation(self):
        annotation_id: int = self.find_annotation_by_text("test12")

        self.assertIsNone(self.annotations.delete_annotation(annotation_id))

    def test_find_annotation_tags(self):
        self.assertIsNotNone(self.annotations.find_annotation_tags())

    def find_annotation_by_text(self, text: str) -> int:
        find_annotation: FindAnnotationObject = FindAnnotationObject(limit=10000)
        for annotation in self.annotations.find_annotations(find_annotation):
            if annotation.get("text") == text:
                return annotation["id"]

    def find_annotation_by_id(self, annotation_id: int, search_field: str) -> str:
        find_annotation: FindAnnotationObject = FindAnnotationObject(limit=10000)
        for annotation in self.annotations.find_annotations(find_annotation):
            if annotation.get("id") == annotation_id:
                return annotation[search_field]
