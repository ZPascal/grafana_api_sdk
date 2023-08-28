import json
import logging
from typing import Union

from .model import APIModel, APIEndpoints, RequestsMethods, CorrelationObject
from .api import Api


class Correlations:
    """The class includes all necessary methods to access the Grafana correlations API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_correlation(self, datasource_uid: str, correlation_uid: str) -> dict:
        """The method includes a functionality to get a specific correlation from a data source - the data source identified by source uid and the correlation uid

         Args:
            datasource_uid (str): Specify the correlation data source uid
            correlation_uid (str): Specify the correlation uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding correlation
        """

        if len(datasource_uid) != 0 and len(correlation_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{datasource_uid}/correlations/{correlation_uid}",
                RequestsMethods.GET,
            )

            if api_call == dict() or api_call.get("description") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_uid or correlation_uid defined.")
            raise ValueError

    def get_all_correlations_by_datasource_uid(self, datasource_uid: str) -> list:
        """The method includes a functionality to get all correlations from a data source - the data source identified by source uid

         Args:
            datasource_uid (str): Specify the correlation data source uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the corresponding correlations
        """

        if len(datasource_uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{datasource_uid}/correlations",
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("description") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_uid defined.")
            raise ValueError

    def get_all_correlations(self) -> list:
        """The method includes a functionality to get all correlations

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the corresponding correlations
        """

        api_call: Union[list, dict] = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.DATASOURCES.value}/correlations", RequestsMethods.GET
        )

        if isinstance(api_call, dict) and (
            api_call == dict()
            or api_call.get("correlations")[0].get("description") is None
        ):
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        elif isinstance(api_call, list) and (
            api_call == list() or api_call[0].get("description") is None
        ):
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def create_correlations(self, correlation_object: CorrelationObject) -> dict:
        """The method includes a functionality to create a correlation between two data sources - the source data source identified by source uid in the path, and the target data source which is specified in the body

         Args:
            correlation_object (CorrelationObject): Specify the correlation object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created correlation
        """

        if (
            len(correlation_object.source_datasource_uid) != 0
            and len(correlation_object.target_datasource_uid) != 0
            and len(correlation_object.label) != 0
            and len(correlation_object.description) != 0
            and len(correlation_object.config_type) != 0
            and len(correlation_object.config_field) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{correlation_object.source_datasource_uid}/correlations",
                RequestsMethods.POST,
                json.dumps(
                    dict(
                        {
                            "targetUID": correlation_object.target_datasource_uid,
                            "label": correlation_object.label,
                            "description": correlation_object.description,
                            "config": {
                                "type": correlation_object.config_type,
                                "field": correlation_object.config_field,
                                "target": correlation_object.config_target,
                            },
                        }
                    )
                ),
            )

            if api_call == dict() or api_call.get("message") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no datasource_uid, target_uid, label, description, config_type or config_field defined."
            )
            raise ValueError

    def delete_correlations(self, source_datasource_uid: str, correlation_uid: str):
        """The method includes a functionality to deletes a correlation

         Args:
            source_datasource_uid (str): Specify the source data source uid
            correlation_uid (str): Specify the correlation uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(source_datasource_uid) != 0 and len(correlation_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{source_datasource_uid}/correlations/{correlation_uid}",
                RequestsMethods.DELETE,
            )

            if "Correlation deleted" != api_call.get("message"):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the correlation.")
        else:
            logging.error(
                "There is no source_datasource_uid or correlation_uid defined."
            )
            raise ValueError

    def update_correlations(
        self,
        source_datasource_uid: str,
        correlation_uid: str,
        label: str,
        description: str,
    ) -> dict:
        """The method includes a functionality to update a correlation

         Args:
            source_datasource_uid (str): Specify the source data source uid
            correlation_uid (str): Specify the correlation uid
            label (str): Specify a label for the correlation
            description (str): Specify a description for the correlation

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated correlation
        """

        if (
            len(source_datasource_uid) != 0
            and len(correlation_uid) != 0
            and len(label) != 0
            and len(description) != 0
        ):
            api_call: any = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{source_datasource_uid}/correlations/{correlation_uid}",
                RequestsMethods.PATCH,
                json.dumps(dict({"label": label, "description": description})),
            )

            if api_call == dict() or api_call.get("message") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no source_datasource_uid, correlation_uid, label or description defined."
            )
            raise ValueError
