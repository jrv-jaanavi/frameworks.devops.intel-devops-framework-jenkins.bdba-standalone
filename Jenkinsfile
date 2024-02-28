pipeline
{
  agent {  label 'win' }
  
  environment{
      ScanCred = credentials('OWR_SCAN_BINARY')
  }

  parameters { string(name: 'ArtifactURL', defaultValue: '', description: 'Artifactory link')
               string(name: 'Artifactpkgname', defaultValue: '', description: 'Artifact package name to be consumed')
  }
  
  stages {
        stage('BDBA') { 
            steps{
                   script{
                   def output =  bat(returnStdout: true, script: "python abi_bdba_scan.py ${ArtifactURL} ${Artifactpkgname}")
                   println "Output from bat execution:" + output
                }   
            }
        } 
        stage('Onekit') { 
            steps{
                   script{
                   def output2 =  bat(returnStdout: true, script: "python  onekitscan.py ${ArtifactURL} ")
                   println "Output from bat execution:" + output2
                }   
            }
        } 
    }
}

  
