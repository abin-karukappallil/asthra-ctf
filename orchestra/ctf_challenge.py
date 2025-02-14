from random import shuffle, randint

def create_ctf_challenge(flag="asthra{skibidi_toilet_rizz}", total_bytes=1000, output_file="orchestra.txt"):

    try:
        with open(output_file, 'w', encoding='utf-8') as h:
            mes = []
            for i in range(total_bytes):
                possibs = list(range(33, 127))
                shuffle(possibs)
                mes.append(chr(possibs[0]))
                
                if i == randint(int(total_bytes * 0.3), int(total_bytes * 0.7)):
                    mes.append(flag)
            
            content = "".join(mes)
            h.write(content)
            print(f"Challenge file created successfully: {output_file}")
            print(f"Total file size: {len(content)} bytes")
            
    except Exception as e:
        print(f"Error creating challenge file: {str(e)}")

if __name__ == "__main__":
    create_ctf_challenge()
    