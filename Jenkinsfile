cat > ~/devops-flask-app/Jenkinsfile << 'EOF'
pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-app"
        VM_NODE1   = "192.168.64.3"
        VM_NODE2   = "192.168.64.4"
    }
    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Bertrussoff/devops-flask-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }
        stage('Trivy Scan') {
            steps {
                sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL ${IMAGE_NAME}:latest'
            }
        }
        stage('Save Image') {
            steps {
                sh 'docker save ${IMAGE_NAME}:latest -o /tmp/flask-app.tar'
            }
        }
        stage('Import Image to k3s Nodes') {
            steps {
                sh '''
                    sudo k3s ctr images import /tmp/flask-app.tar
                    scp /tmp/flask-app.tar bert@${VM_NODE1}:/tmp/flask-app.tar
                    ssh bert@${VM_NODE1} "sudo k3s ctr images import /tmp/flask-app.tar"
                    scp /tmp/flask-app.tar bert@${VM_NODE2}:/tmp/flask-app.tar
                    ssh bert@${VM_NODE2} "sudo k3s ctr images import /tmp/flask-app.tar"
                '''
            }
        }
        stage('Deploy to k3s') {
            steps {
                sh 'kubectl rollout restart deployment flask-app'
            }
        }
        stage('Verify Deployment') {
            steps {
                sh 'kubectl rollout status deployment flask-app'
                sh 'kubectl get pods'
            }
        }
    }
    post {
        success {
            echo 'Deployment successful on k3s! 🚀'
        }
        failure {
            echo 'Deployment failed! Check the logs.'
        }
    }
}
EOF
