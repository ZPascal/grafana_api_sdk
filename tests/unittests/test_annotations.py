from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import (
    APIModel,
    FindAnnotationObject,
    AnnotationObject,
    AnnotationGraphiteObject,
)
from src.grafana_api.annotations import Annotations


class AnnotationsTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotations(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"id": "test"}]),
            annotations.find_annotations(),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotations_filter_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"id": "test"}]),
            annotations.find_annotations(
                FindAnnotationObject(
                    from_value=1000,
                    to_value=1000,
                    limit=1000,
                    alert_id=1,
                    dashboard_id=1,
                    panel_id=1,
                    user_id=1,
                    type="alert",
                    tags=list(["test", "test1"]),
                )
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotations_no_valid_filter_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"id": "test"}]),
            annotations.find_annotations(
                FindAnnotationObject(
                    from_value=None,
                    to_value=None,
                    limit=100,
                    alert_id=None,
                    dashboard_id=None,
                    panel_id=None,
                    user_id=None,
                    type=None,
                    tags=None,
                )
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotations_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.find_annotations()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_annotation(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Annotation added", "id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            1,
            annotations.create_annotation(
                AnnotationObject(
                    dashboard_uid="test",
                    panel_id=1,
                    time=1000,
                    time_end=1000,
                    tags=["test", "test"],
                    text="test",
                )
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_annotation_no_annotation_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            annotations.create_annotation(None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_annotation_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.create_annotation(
                AnnotationObject(
                    dashboard_uid=None,
                    panel_id=None,
                    time=1000,
                    time_end=1000,
                    tags=["test", "test"],
                    text="test",
                )
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_graphite_annotation(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict({"message": "Graphite annotation added", "id": 1})
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(
            1,
            annotations.create_graphite_annotation(
                AnnotationGraphiteObject(
                    what="test", tags=["test", "test"], when=1000, data="test"
                )
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_graphite_annotation_no_annotation_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            annotations.create_graphite_annotation(None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_graphite_annotation_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.create_graphite_annotation(
                AnnotationGraphiteObject(
                    what="test", tags=["test", "test"], when=None, data=None
                )
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_annotation(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Annotation patched"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            annotations.update_annotation(
                1,
                AnnotationObject(
                    dashboard_uid="test",
                    panel_id=1,
                    time=1000,
                    time_end=1000,
                    tags=["test", "test"],
                    text="test",
                ),
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_annotation_no_annotation_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            annotations.update_annotation(0, None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_annotation_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.update_annotation(
                1,
                AnnotationObject(
                    dashboard_uid=None,
                    panel_id=None,
                    time=None,
                    time_end=None,
                    tags=None,
                    text=None,
                ),
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_annotation(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Annotation deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            annotations.delete_annotation(1),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_annotation_no_annotation_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            annotations.delete_annotation(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_annotation_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.delete_annotation(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotation_tags(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            annotations.find_annotation_tags(tag="test", limit=1000),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotation_tags_only_limit(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            annotations.find_annotation_tags(limit=1000),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotation_tags_only_tag(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            annotations.find_annotation_tags(tag="test"),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_find_annotation_tags_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        annotations: Annotations = Annotations(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            annotations.find_annotation_tags()
