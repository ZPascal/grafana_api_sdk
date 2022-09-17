import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
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

    def create_correlations(
        self,
        source_datasource_uid: str,
        target_datasource_uid: str,
        label: str,
        description: str,
    ) -> dict:
        """The method includes a functionality to create a correlation between two data sources - the source data source identified by source uid in the path, and the target data source which is specified in the body

         Args:
            source_datasource_uid (str): Specify the source data source uid
            target_datasource_uid (str): Specify the target data source uid
            label (str): Specify a label for the correlation
            description (str): Specify a description for the correlation

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created correlation
        """

        if (
            len(source_datasource_uid) != 0
            and len(target_datasource_uid) != 0
            and len(label) != 0
            and len(description) != 0
        ):
            api_call: dict = (
                Api(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.DATASOURCES.value}/uid/{source_datasource_uid}/correlations",
                    RequestsMethods.POST,
                    json.dumps(
                        dict(
                            {
                                "targetUID": target_datasource_uid,
                                "label": label,
                                "description": description,
                            }
                        )
                    ),
                )
                .json()
            )

            if api_call == dict() or api_call.get("message") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no datasource_uid, target_uid, label or description defined."
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
            api_call: dict = (
                Api(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.DATASOURCES.value}/uid/{source_datasource_uid}/correlations/{correlation_uid}",
                    RequestsMethods.DELETE,
                )
                .json()
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

            if api_call.json() == dict() or api_call.json().get("message") is None:
                logging.error(f"Check the error: {api_call.json()}.")
                raise Exception
            else:
                return api_call.json()
        else:
            logging.error(
                "There is no source_datasource_uid, correlation_uid, label or description defined."
            )
            raise ValueError
