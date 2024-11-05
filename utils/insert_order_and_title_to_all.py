# this script was used to add an order to the top 
# of the mark down files. 
# 
# You can read more about `order` in quarto here: 
# https://quarto.org/docs/websites/website-navigation.html#:~:text=Order%20is%20alphabetical%20(by%20filename)%20unless%20a%20numeric%20order%20field%20is%20provided%20in%20document%20metadata

import os 

def fix_file(filename: str): 
    data = None 
    with open(filename, 'r') as f: 
        data = f.read() 
    
    new_title = filename.strip()[:-3] # i.e. ignore the ".md" part.
    # if the filename is `2.3.md` for example
    # the following variable will hold the number
    # 3.
    the_order_of_the_file = filename.strip().split('.')[1]
    
    # get the end of the first line.
    new_header  = f"---\norder: {the_order_of_the_file}\n"
    new_header += f"title: {new_title!r}\n"
    new_header +=  "---\n"
    
    new_data = new_header + data

    with open(filename, 'w') as f: 
        f.write(new_data)
    
    print(f"[+] successfully updated {filename}")

def get_file_names_that_begin_with_ch():
    all_filenames = os.listdir() 
    return filter(lambda f : f.startswith('Ch'),all_filenames)

if __name__ == '__main__': 
    for ch_dir in get_file_names_that_begin_with_ch():
        os.chdir(ch_dir)
        
        all_md_filenames = os.listdir()

        for single_file in all_md_filenames:
            if not single_file.endswith('.md'):
                continue
            fix_file(single_file)

        os.chdir('..')