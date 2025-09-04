#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(bslib)


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
      )
    )
  )
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
  output$msb_switch <- renderUI({
    label <- if (input$twoscomp) "-128" else "128"
    input_switch("eight", label)
  })
}

shinyApp(ui = ui, server = server)
