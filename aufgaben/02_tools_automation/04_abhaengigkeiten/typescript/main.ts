import axios from "axios";
import * as dayjs from "dayjs";

async function run() {
  try {
    const res = await axios.get("https://icanhazdadjoke.com/", {
      headers: { Accept: "text/plain" },
    });

    console.log("Dad Joke:", res.data);
    console.log("Timestamp:", dayjs().format("YYYY-MM-DD HH:mm:ss"));
  } catch (err) {
    console.error("es kracht:", err);
  }
}

run();
