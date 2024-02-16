@Library(['abi@3.0', 'idf-enabling@3.0.0']) _
pipeline
{
  agent {  label 'win' }

  parameters { string(name: 'ArtifactURL', defaultValue: '', description: 'Artifactory link') }
  
  stages {
        stage('BDBA') { 
            steps{
                     abi_scan_binary(timeout: 40,
                            wait: true,
                            report_name: "BDBA",
                            include_components: true,
                            artifact_pkg_name: "Sample",
                           )
                }
          }
      }
}
