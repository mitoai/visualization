def visualizationImage = 'eu.gcr.io/ntnu-smartmedia/visualization'

defaultPodTemplate {
  python36Template {
    lastTemplate('visualization') {
      def scmVars

      stage("Checkout source") {
        scmVars = checkout scm
      }

      stage("Test") {

      }

      stage("Build") {
        dockerBuildAndPush image: visualizationImage, tag: scmVars.GIT_COMMIT, path: '.'
      }
    }
  }
}
