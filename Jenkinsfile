pipeline
{
  agent {  label 'win' }

  parameters { string(name: 'ArtifactURL', defaultValue: '', description: 'Artifactory link') }
  
  stages {
        stage('BDBA') { 
            steps{
                    withCredentials([usernamePassword(credentialsId: 'OWR_SCAN', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                     bat '''
                          C:\\OWR\\Tools\\wit.exe sync-V2 -o samplewin  -m "Manifest.xml"
                          pip install --upgrade pip
                          pip install  abi==3.0.0 --extra-index-url=https://ubit-artifactory-or.intel.com/artifactory/api/pypi/one-windows-pypi-local/simple --proxy="http://proxy-chain.intel.com:912
                          abi binary scan --timeout 40 --wait  --report_name SampleWin --include_components  --zip_file SampleWin_1.0.00.7349.zip --username USERNAME --password "\"${PASSWORD}\"" 
                     '''
                }
          }
      }
}
