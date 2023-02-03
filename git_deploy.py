from prefect.deployments import Deployment
from etl_web_to_gcs_gh import etl_web_to_gcs
from prefect.filesystems import GitHub

github_block = GitHub.load("zommgh")

deployment = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="github",
)

if __name__ == "__main__":
    deployment.apply()