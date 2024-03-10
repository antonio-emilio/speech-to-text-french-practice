import speech_recognition as sr

def transcrever_audio():
    # Crie um reconhecedor de fala
    recognizer = sr.Recognizer()

    # Abra o arquivo de saída em modo de escrita
    with open("transcricoes.txt", "w") as f:
        while True:
            try:
                # Use o microfone padrão como fonte de áudio
                with sr.Microphone() as source:
                    print("Diga algo em francês:")
                    # Ajuste o ruído do ambiente para reduzir o ruído de fundo e melhorar a precisão
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    # Ouça o áudio do microfone
                    audio = recognizer.listen(source, timeout=5)

                transcrição = recognizer.recognize_google(audio, language='fr-FR')
                print("Transcrição: " + transcrição)
                
                # Escreva a transcrição no arquivo
                f.write(transcrição + "\n")
                f.flush()  # Certifique-se de que os dados são escritos imediatamente
            except sr.WaitTimeoutError:
                pass  # Continuar esperando por áudio
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio")
            except sr.RequestError as e:
                print("Erro ao fazer a solicitação; {0}".format(e))
            except KeyboardInterrupt:
                print("Encerrando o programa...")
                break

if __name__ == "__main__":
    transcrever_audio()
