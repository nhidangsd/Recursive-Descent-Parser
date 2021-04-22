# Recursive-Descent-Parser


A simple recursive descent parser that can validate and evaluate expressions based on this specified EBNF grammar rule: 
> <li> < relop >  ::=  < | > | <= | >= | = | != | not </li>
> <li> < expr >   ::=  < term > { (and|or) < term > }  </li>
> <li> < term >   ::= (< expr >) | < relop > < factor > | < factor > - < factor >   </li>
> <li> < factor > ::=  int  </li>





<!-- TABLE OF CONTENTS -->
## Table of Contents

  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## 1. About The Project





### Built With
* [Python](https://www.python.org)



<!-- GETTING STARTED -->
## 2. Getting Started


### Installation

1. Clone the repo
   ```sh
   https://github.com/nhidangsd/Recursive-Descent-Parser.git
   ```
2. Run the program
   ```sh
   python3 main.py
   ```


<!-- USAGE EXAMPLES -->
## Usage

Read `main.py` for more details.
Example:
``` Python
# Define a string
expr = '7-17'   
# Create an instance of resDecsent and pass the defined string as an argument
r = recDecsent(expr)
# Check if the string is valid, this will print True as '7 - 17' is a valid expression
print(r.validate())

```

