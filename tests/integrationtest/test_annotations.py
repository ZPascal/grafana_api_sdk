import os
from unittest import TestCase

from src.grafana_api.model import (
    APIModel,
    AnnotationObject,
    AnnotationGraphiteObject,
)
from src.grafana_api.annotations import Annotations


class AnnotationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    annotations: Annotations = Annotations(model)

    def test_a_find_annotations(self):
        self.assertEqual(101, self.annotations.find_annotations()[0].get("id"))

    def test_b_create_annotation(self):
        annotations: AnnotationObject = AnnotationObject(
            dashboard_uid="test1",
            time=1000,
            time_end=10000,
            tags=["test"],
            text="test1",
        )
        self.assertIsNotNone(self.annotations.create_annotation(annotations))
        length: int = len(self.annotations.find_annotations())

        self.assertEqual(
            "test1", self.annotations.find_annotations()[length - 1].get("dashboardUID")
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

        length: int = len(self.annotations.find_annotations())

        self.assertIsNone(
            self.annotations.update_annotation(
                self.annotations.find_annotations()[length - 2].get("id"), annotations
            )
        )
        self.assertEqual(
            "test12", self.annotations.find_annotations()[length - 2].get("text")
        )

    def test_e_delete_annotation(self):
        length: int = len(self.annotations.find_annotations())
        self.assertIsNone(
            self.annotations.delete_annotation(
                self.annotations.find_annotations()[length - 1].get("id")
            )
        )

    def test_find_annotation_tags(self):
        self.assertIsNotNone(self.annotations.find_annotation_tags())
