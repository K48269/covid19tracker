pipeline {
    agent any

    parameters {
        string(name: "TEST_STRING", defaultValue: "",  description: "")
        string(name: "TEST_PASSWORD", defaultValue: "", description: "")
    }

    stages {
        stage('Hello') {
            steps {
                git branch: 'main', url: 'https://github.com/K48269/covid19tracker.git'
            }
        }
        
        stage('Ansible Playbook execution') {
            steps {
                echo 'Hello kiran'
                ansiblePlaybook installation: 'Ansible', limit: 'localhost', playbook: '/tmp/text_jenkins.yaml'
            }
        }
        
        stage('build Docker Image And Pushing') {
            steps {
                sh 'docker build -t kiranreddy912161/one .'
                sh 'docker login -u "$TEST_STRING" -p"$TEST_PASSWORD"'
                sh 'docker push kiranreddy912161/one:latest'
            }
        }

    }
}
