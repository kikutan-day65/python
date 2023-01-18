from translate import Translator

translator= Translator(to_lang="ja")
try:
    with open("./exercise.txt", mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        
        with open("./translated.txt", mode='w') as my_file2:
            # expected to be translated into japanese, but garbled text. why?
            my_file2.write(translation)

except FileNotFoundError as e:
    print("check your file path")