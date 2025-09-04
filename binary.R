
library(shiny)
library(bslib)

ascii_table <- c(
  "NUL","SOH","STX","ETX","EOT","ENQ","ACK","BEL",
  "BS","HT","LF","VT","FF","CR","SO","SI",
  "DLE","DC1","DC2","DC3","DC4","NAK","SYN","ETB",
  "CAN","EM","SUB","ESC","FS","GS","RS","US",
  " ","!","\"","#","$","%","&","'","(",")","*","+",
  ",","-",".","/","0","1","2","3","4","5","6","7",
  "8","9",":",";","<","=",">","?","@","A","B","C",
  "D","E","F","G","H","I","J","K","L","M","N","O",
  "P","Q","R","S","T","U","V","W","X","Y","Z","[",
  "\\","]","^","_","`","a","b","c","d","e","f","g",
  "h","i","j","k","l","m","n","o","p","q","r","s",
  "t","u","v","w","x","y","z","{","|","}","~","DEL"
)

ascii_lookup <- function(n) {
  if (n < 0 || n > 127) return("")
  ascii_table[n + 1]  
}

theme <- bs_theme(
  bg = "#164F73", fg = "white", primary = "#FCC780",
  base_font = font_google("Architects Daughter"),
  code_font = font_google("Space Mono")
)



ui <- page_fluid(
  theme = theme,
  titlePanel(title = "Mr Andrew's Binary Counter!", windowTitle = "binary counter"),
  layout_columns(
    card(
      card(
      input_switch("twoscomp", "Two’s complement (MSB = −128)?")),
      card(
      # input_switch("eight", uiOutput(twos())),
      uiOutput("msb_switch"),   
      input_switch("seven", "64"),
      input_switch("six", "32"),
      input_switch("five", "16"),
      input_switch("four", "8"),
      input_switch("three", "4"),
      input_switch("two", "2"),
      input_switch("one", "1")
      ) # inner card
    ), #outer card
    #verbatimTextOutput("binary"),
    card(
      value_box(
        value = textOutput("binary"),
        #value = uiOutput("save"),
        title = "Your Binary Code"
      ),
      value_box(
        value = textOutput("value"),
        #value = uiOutput("save"),
        title = "Your Decimal Value"
      ), #value box
      value_box(
        value = textOutput("ascii"),
        title = "ASCII representation"
      )
    )
    
  )
  # verbatimTextOutput("value")
)

server <- function(input, output) {
  twos <- reactive(
    if (input$twoscomp) -128 else 128
  )
  
  output$binary <- renderText({
    paste0(
      as.numeric(input$eight),
      as.numeric(input$seven),
      as.numeric(input$six),
      as.numeric(input$five),
      as.numeric(input$four),
      as.numeric(input$three),
      as.numeric(input$two),
      as.numeric(input$one)
    )
    
  })
  output$value <- renderText({
      input$eight*twos() + 
      input$seven*64 +
      input$six*32 +
      input$five*16 +
      input$four*8 +
      input$three*4 +
      input$two*2 +
      input$one*1
      })
  output$ascii <- renderText({
    n_ascii <- as.numeric(input$eight)*128 + 
      input$seven*64 +
      input$six*32 +
      input$five*16 +
      input$four*8 +
      input$three*4 +
      input$two*2 +
      input$one*1
    ascii_lookup(n_ascii)
  })
  output$msb_switch <- renderUI({
    label <- if (input$twoscomp) "-128" else "128"
    input_switch("eight", label)
  })
}

shinyApp(ui = ui, server = server)
