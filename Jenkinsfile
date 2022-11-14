pipeline{
	agent {
  		label 'home-server'
	}
	
	environment {
		DOCKERHUB_CREDENTIALS = credentials('dockerhub')
		REMOTE_SERVER_DOMAIN = "node-1.silk-cat.software"
		NODE_1_CREDENTIALS = credentials('NODE_1')
	}

	stages {
        stage('Git clone') {
			steps {
				git branch: 'main', url: 'git@github.com:hovanvydut/pbl6-ai.git', credentialsId: 'HOME_SERVER_SSH_PRIVATE_KEY'
			}
		}

		stage('Build and run container') {
			steps {
				script {
					sh '''
                        make dc-up
					'''
				}
			}
		}
	}

	post {
		always {
            echo 'Always message'
		}

		success {
            echo 'Success message'
        }

		failure {
            echo 'Failed :( message'
        }

        changed {
            echo 'Things were different before...'
        }

		aborted  {
			echo "Aborted message"
		}
	}
}