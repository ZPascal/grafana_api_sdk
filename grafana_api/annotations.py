import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    AnnotationObject,
    AnnotationGraphiteObject,
    FindAnnotationObject,
)
from .api import Api


class Annotations:
    """The class includes all necessary methods to access the Grafana annotations API endpoints. Annotations can be organization annotations that can be shown on any dashboard by configuring an annotation data source filtered by tags. They can also be tied to a panel on a dashboard and are then only shown on that panel

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def find_annotations(self, annotation: FindAnnotationObject = None) -> list:
        """The method includes a functionality to find the corresponding annotations

        Args:
            annotation (FindAnnotationObject): Specify the find annotation object

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the result of the find annotations call
        """

        custom_query: str = "?"

        if annotation is not None:
            if annotation.from_value is not None and annotation.from_value != 0:
                custom_query = f"from={annotation.from_value}"

            if annotation.to_value is not None and annotation.to_value != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}to={annotation.to_value}"

            if annotation.limit != 100 and annotation.limit != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}limit={annotation.limit}"

            if annotation.alert_id is not None and annotation.alert_id != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}alertId={annotation.alert_id}"

            if annotation.dashboard_id is not None and annotation.dashboard_id != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}dashboardId={annotation.dashboard_id}"

            if annotation.panel_id is not None and annotation.panel_id != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}panelId={annotation.panel_id}"

            if annotation.user_id is not None and annotation.user_id != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}userId={annotation.user_id}"

            if annotation.type is not None and len(annotation.type) != 0:
                custom_query = Api.prepare_api_string(custom_query)
                custom_query = f"{custom_query}type={annotation.type}"

            if annotation.tags is not None:
                custom_query = Api.prepare_api_string(custom_query)

                tags_string: str = ""
                for i in range(0, len(annotation.tags)):
                    tags_string = f"{tags_string}tags={annotation.tags[i]}"

                    if i < len(annotation.tags) - 1:
                        tags_string = f"{tags_string}&"

                custom_query = f"{custom_query}{tags_string}"

        if len(custom_query) == 1:
            custom_query = ""

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ANNOTATIONS.value}{custom_query}",
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def create_annotation(
        self,
        annotation: AnnotationObject,
    ) -> int:
        """The method includes a functionality to create the corresponding annotation

        Args:
            annotation (AnnotationObject): Specify the annotation object

        Required Permissions:
            Action: annotations:create
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the annotation id
        """

        if (
            annotation is not None
            and annotation.time != 0
            and annotation.time_end != 0
            and len(annotation.text) != 0
            and len(annotation.tags) != 0
        ):
            annotation_object: dict = dict(
                {
                    "time": annotation.time,
                    "timeEnd": annotation.time_end,
                    "tags": annotation.tags,
                    "text": annotation.text,
                }
            )

            if annotation.dashboard_uid is not None:
                annotation_object.update(
                    dict({"dashboardUID": annotation.dashboard_uid})
                )

            if annotation.panel_id is not None:
                annotation_object.update(dict({"panelId": annotation.panel_id}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.ANNOTATIONS.value,
                RequestsMethods.POST,
                json.dumps(annotation_object),
            )

            if (
                api_call.get("message") != "Annotation added"
                or api_call.get("id") is None
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return int(api_call.get("id"))
        else:
            logging.error("There is no time, time_end, text or tags defined.")
            raise ValueError

    def create_graphite_annotation(self, annotation: AnnotationGraphiteObject) -> int:
        """The method includes a functionality to create the corresponding graphite annotation

        Args:
            annotation (AnnotationGraphiteObject): Specify the annotation object

        Required Permissions:
            Action: annotations:create
            Scope: annotations:type:organization

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the annotation id
        """

        if (
            annotation is not None
            and len(annotation.what) != 0
            and len(annotation.tags) != 0
        ):
            annotation_object: dict = dict(
                {"what": annotation.what, "tags": annotation.tags}
            )

            if annotation.when is not None:
                annotation_object.update(dict({"when": annotation.when}))

            if annotation.data is not None:
                annotation_object.update(dict({"data": annotation.data}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ANNOTATIONS.value}/graphite",
                RequestsMethods.POST,
                json.dumps(annotation_object),
            )

            if (
                api_call.get("message") != "Graphite annotation added"
                or api_call.get("id") is None
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return int(api_call.get("id"))
        else:
            logging.error("There is no what or tags defined.")
            raise ValueError

    def update_annotation(self, id: int, annotation: AnnotationObject):
        """The method includes a functionality to update the corresponding annotation specified by the annotation id

        Args:
            id (int): Specify the annotation object id
            annotation (AnnotationObject): Specify the annotation object

        Required Permissions:
            Action: annotations:write
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and annotation is not None:
            annotation_object: dict = dict()

            if annotation.time is not None and annotation.time != 0:
                annotation_object.update(dict({"time": annotation.time}))

            if annotation.time_end is not None and annotation.time_end != 0:
                annotation_object.update(dict({"timeEnd": annotation.time_end}))

            if annotation.text is not None and len(annotation.text) != 0:
                annotation_object.update(dict({"text": annotation.text}))

            if annotation.tags is not None and len(annotation.tags) != 0:
                annotation_object.update(dict({"text": annotation.text}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ANNOTATIONS.value}/{id}",
                RequestsMethods.PATCH,
                json.dumps(annotation_object),
            )

            if api_call.get("message") != "Annotation patched":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the annotation.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def delete_annotation(
        self,
        id: int,
    ):
        """The method includes a functionality to delete the corresponding annotation specified by the annotation id

        Args:
            id (int): Specify the annotation object id

        Required Permissions:
            Action: annotations:write
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ANNOTATIONS.value}/{id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Annotation deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the annotation.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def find_annotation_tags(
        self,
        tag: str = None,
        limit: int = 100,
    ):
        """The method includes a functionality to find the annotation tags

        Args:
            tag (str): Specify the optional annotation tag
            limit (int): Specify the optional annotation limit (default 100)

        Required Permissions:
            Action: annotations:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the find annotation tags call
        """

        filter_values: str = ""

        if tag is not None and len(tag) != 0:
            filter_values = f"?tag={tag}"

        if limit != 100:
            if tag is None:
                filter_values = "?"

            if len(filter_values) == 1:
                filter_values = f"{filter_values}limit={limit}"
            else:
                filter_values = f"{filter_values}&limit={limit}"

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ANNOTATIONS.value}/tags{filter_values}",
        )

        if api_call == dict() or api_call.get("result") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call
