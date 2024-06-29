def generate_header_file (author, class_name):
    from datetime import datetime

    now = datetime.now()
    date = now.strftime("%c")

    h_code = f"""
#pragma once
/*********************************************/
// 
//           CopyRight {author}
//
/*********************************************/
/*
author: {author}
date: {date}
*/
namespace svm {{
class {class_name}{{

public:
    {class_name}();
    ~{class_name}();

private:
}};
}}"""
    return h_code


def generate_source_file (author, class_name):
    from datetime import datetime

    now = datetime.now()
    date = now.strftime("%c")

    cpp_code = f"""
#pragma once
/*********************************************/
// 
//           CopyRight {author}
//
/*********************************************/
/*
author: {author}
date: {date}
*/
#include "{class_name}.h"

namespace svm {{
    {class_name}::{class_name}(){{}}
    {class_name}::~{class_name}(){{}}
}}
"""
    return cpp_code

author = "Mostafa El-Bahrawy"
class_name = input("Enter the class name that you want to create: ")

h_code = generate_header_file(author, class_name)
cpp_code = generate_source_file(author, class_name)

with open(f"{class_name}.h", 'w') as header_file:
    header_file.write(h_code)

with open(f"{class_name}.cpp", 'w') as source_file:
    source_file.write(cpp_code)