#!/usr/bin/env python3

def check_flag(submitted_flag):

    correct_flag = "asthra{skibidi_toilet_rizz}"
    
    submitted_flag = submitted_flag.strip().lower()
    
    if not submitted_flag.startswith("asthra{") or not submitted_flag.endswith("}"):
        return False, "Invalid flag format! Flag should be in format: asthra{...}"
    
    if submitted_flag == correct_flag:
        return True, "🎉 Congratulations! Flag is correct!"
    else:
        return False, "❌ Incorrect flag. Try again!"

def main():
    print("=== CTF Flag Submission ===")
    print("Enter the flag you found (format: asthra{...})")
    
    while True:
        flag = input("\nSubmit flag (or 'quit' to exit): ")
        
        if flag.lower() == 'quit':
            print("Goodbye!")
            break
            
        success, message = check_flag(flag)
        print(message)

if __name__ == "__main__":
    main()