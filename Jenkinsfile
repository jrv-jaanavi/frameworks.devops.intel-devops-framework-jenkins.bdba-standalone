pipeline
{
  agent {  label 'win' }

  parameters { string(name: 'ArtifactURL', defaultValue: '', description: 'Artifactory link')
               string(name: 'Artifactpkgname', defaultValue: '', description: 'Artifact package name to be consumed')
  }
  
  stages {
        stage('BDBA') { 
           environment{
                  ScanCred = credentials('OWR_SCAN_BINARY')
                }
            steps{
                   script{
                   def output1 =  bat(returnStdout: true, script: "python abi_bdba_scan.py ${ArtifactURL} ${Artifactpkgname}")
                   println "Output from ABI execution:" + output1
                }   
            }
        } 
        stage('Onekit-Central') { 
            steps{
                   script{
                   def output2 =  bat(returnStdout: true, script: "python onekitscan.py ${ArtifactURL} ")
                   println "Output from Central Scan execution:" + output2
                }   
            }
        } 

     stage('OneKitscan') { 
          environment{
                 Authtoken = credentials('OWR_Authtoken')
                }
            steps{
                   script{
                   def output3 =  bat(returnStdout: true, script: "python onekitbdbascan.py ")
                   println "Output from OneKit Scan execution:" + output3
                }   
            }
        } 
    }
}

  
