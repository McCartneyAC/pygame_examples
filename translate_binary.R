# challenged a student to translate strings of bytes to ASCII then felt the need, for some odd reason, to do the same in R. 

library(tibble)
table<-tribble(
  ~Dec, ~Binary,~Char,~Description,
0,"00000000","NUL","Null",
1,"00000001","SOH","Start of Heading",
2,"00000010","STX","Start of Text",
3,"00000011","ETX","End of Text",
4,"00000100","EOT","End of Transmission",
5,"00000101","ENQ","Enquiry",
6,"00000110","ACK","Acknowledge",
7,"00000111","BEL","Bell",
8,"00001000","BS","Backspace",
9,"00001001","HT","Horizontal Tab",
10,"00001010","LF","Line Feed",
11,"00001011","VT","Vertical Tab",
12,"00001100","FF","Form Feed",
13,"00001101","CR","Carriage Return",
14,"00001110","SO","Shift Out",
15,"00001111","SI","Shift In",
16,"00010000","DLE","Data Link Escape",
17,"00010001","DC1","Device Control 1",
18,"00010010","DC2","Device Control 2",
19,"00010011","DC3","Device Control 3",
20,"00010100","DC4","Device Control 4",
21,"00010101","NAK","Negative Acknowledge",
22,"00010110","SYN","Synchronize",
23,"00010111","ETB","End of Transmission Block",
24,"00011000","CAN","Cancel",
25,"00011001","EM","End of Medium",
26,"00011010","SUB","Substitute",
27,"00011011","ESC","Escape",
28,"00011100","FS","File Separator",
29,"00011101","GS","Group Separator",
30,"00011110","RS","Record Separator",
31,"00011111","US","Unit Separator",
32,"00100000"," ","Space",
33,"00100001","!","exclamation mark",
34,"00100010","'","double quote",
35,"00100011","#","number",
36,"00100100","$","dollar",
37,"00100101","%","percent",
38,"00100110","&","ampersand",
39,"00100111","'","single quote",
40,"00101000","(","left parenthesis",
41,"00101001",")","right parenthesis",
42,"00101010","*","asterisk",
43,"00101011","+","plus",
44,"00101100",",","comma",
45,"00101101","-","minus",
46,"00101110",".","period",
47,"00101111","/","slash",
48,"00110000","0","zero",
49,"00110001","1","one",
50,"00110010","2","two",
51,"00110011","3","three",
52,"00110100","4","four",
53,"00110101","5","five",
54,"00110110","6","six",
55,"00110111","7","seven",
56,"00111000","8","eight",
57,"00111001","9","nine",
58,"00111010",":","colon",
59,"00111011",";","semicolon",
60,"00111100","<","less than",
61,"00111101","=","equality sign",
62,"00111110",">","greater than",
63,"00111111","?","question mark",
64,"01000000","@","at sign",
65,"01000001","A","NA",
66,"01000010","B","NA",
67,"01000011","C","NA",
68,"01000100","D","NA",
69,"01000101","E","NA",
70,"01000110","F","NA",
71,"01000111","G","NA",
72,"01001000","H","NA",
73,"01001001","I","NA",
74,"01001010","J","NA",
75,"01001011","K","NA",
76,"01001100","L","NA",
77,"01001101","M","NA",
78,"01001110","N","NA",
79,"01001111","O","NA",
80,"01010000","P","NA",
81,"01010001","Q","NA",
82,"01010010","R","NA",
83,"01010011","S","NA",
84,"01010100","T","NA",
85,"01010101","U","NA",
86,"01010110","V","NA",
87,"01010111","W","NA",
88,"01011000","X","NA",
89,"01011001","Y","NA",
90,"01011010","Z","NA",
91,"01011011","[","NA",
92,"01011100","\\","NA",
93,"01011101","]","NA",
94,"01011110","^","NA",
95,"01011111","_","NA",
96,"01100000","'","NA",
97,"01100001","a","NA",
98,"01100010","b","NA",
99,"01100011","c","NA",
100,"01100100","d","NA",
101,"01100101","e","NA",
102,"01100110","f","NA",
103,"01100111","g","NA",
104,"01101000","h","NA",
105,"01101001","i","NA",
106,"01101010","j","NA",
107,"01101011","k","NA",
108,"01101100","l","NA",
109,"01101101","m","NA",
110,"01101110","n","NA",
111,"01101111","o","NA",
112,"01110000","p","NA",
113,"01110001","q","NA",
114,"01110010","r","NA",
115,"01110011","s","NA",
116,"01110100","t","NA",
117,"01110101","u","NA",
118,"01110110","v","NA",
119,"01110111","w","NA",
120,"01111000","x","NA",
121,"01111001","y","NA",
122,"01111010","z","NA",
123,"01111011","{","left curly bracket",
124,"01111100","|","vertical bar",
125,"01111101","}","right curly bracket",
126,"01111110","~","tilde",
127,"01111111","DEL","delete"
)
translate_bin_to_int <- function(x){
  if (is.character(x) == 0)
    print("x must be a binary string")
  bnary <- c(128,64,32,16,8,4,2,1)

  listx<-strsplit(x, split = "")
  for (i in listx){
    ynew <- as.numeric(i)
  }
  sum(ynew*bnary)
}


translate_int_to_char<- function(n){
  table |> 
    dplyr::filter(Dec==n) |> 
    dplyr::select(Char) |> 
    as.character() |> 
    cat()
}


translate<-function(txt){
    text_list <- strsplit(txt, split = " ")
    codes <- text_list[[1]]
    for (i in 1:length(codes)){
      codes[i] |> 
      translate_bin_to_int() |> 
      translate_int_to_char() |> 
      cat()
    }

}
translate("01001001 00100000 01101000 01100001 01110100 01100101 00100000 01100001 01110011 01100011 01101001 01101001 00100000 00111010 00101000")


