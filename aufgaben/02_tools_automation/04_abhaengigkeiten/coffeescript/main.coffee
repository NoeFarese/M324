axios = require "axios"
dayjs = require "dayjs"

run = ->
  try
    res = await axios.get "https://icanhazdadjoke.com/",
      headers:
        Accept: "text/plain"

    console.log "Dad Joke:", res.data
    console.log "Timestamp:", dayjs().format("YYYY-MM-DD HH:mm:ss")
  catch err
    console.error "Bro... no joke today:", err

run()
