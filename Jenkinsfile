pipeline {
    agent any
    
    parameters {
        choice(
            name: 'Opcion',
            choices: ['Trivia', 'Procesar Pedidos', 'Consultas USQL'],
            description: '---------- Elige una opción para ejecutar -------------'
        )
    }

    
    stages {
        stage('Selección de Opción') {
            steps {
                script {
                    echo "--------------------------------------"
                    echo "Opción seleccionada: ${params.Opcion}"
                    echo "--------------------------------------"
                }
            }
        }

        stage('Instalar Dependencias') {
            steps {
                dir('Entregable1') {

                    // Acá tuve que poner la ubicación entera de python.exe porque no me lo reconocía como comando
                    bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Ejecutar Opción Seleccionada') {
            steps {
                script {
                    if (params.Opcion == 'Trivia') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando el juego de Trivia...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al trivia
                        
                        dir('Entregable1') {

                            // Mismo tema con la ubicación de python.exe
                            bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe Principal.py'
                        }
                        
                    } else if (params.Opcion == 'Procesar Pedidos') {
                        
                        echo "--------------------------------------"
                        echo 'Procesando pedidos...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al procesamiento de pedidos

                        dir('Entregable2/src') {
                            bat 'javac PlantaDeProduccion.java'
                            bat 'java PlantaDeProduccion'
                        }

                    } else if (params.Opcion == 'Consultas USQL') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando consultas USQL...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente a las consultas USQL

                        dir('Entregable3') {
                            bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe TraductorConsultas.py'
        
                        // Estando adentro de la carpeta Entregable3, se ejecuta LexerMain.py
                            dir('Lexer') {
                                bat 'C:\\Users\\ignac\\AppData\\Local\\Programs\\Python\\Python310\\python.exe LexerMain.py'
                            }
                        }
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo "--------------------------------------"
            echo 'Pipeline completado con éxito.'
            echo "--------------------------------------"

            emailext(
            subject: "Pipeline completado con éxito",
            body: """Hubo un error durante la ejecución del pipeline.
            
            Opción seleccionada: ${params.Opcion}
            
            Los detalles de la ejecución se pueden ver en Jenkins.""",
            
            recipientProviders: [[$class: 'RequesterRecipientProvider']]

            // Si no se manda el mail, se puede usar:
            // to: 'nombre@ejemplo.com' en lugar de la línea del recipientProviders
            
            )
        }
        failure {
            echo "--------------------------------------"
            echo 'Hubo un error en el pipeline.'
            echo "--------------------------------------"

            emailext(
            subject: "Error en el pipeline",
            body: """Hubo un error durante la ejecución del pipeline.
            
            Opción seleccionada: ${params.Opcion}
            
            Revise los detalles de la ejecución en Jenkins para más información.""",
            recipientProviders: [[$class: 'RequesterRecipientProvider']]
            )
        }
    }
}