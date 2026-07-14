fetch("data/events.json")
  .then(response => response.json())
  .then(events => {
    const eventArea = document.getElementById("event-list");

    events.forEach(event => {
      const div = document.createElement("div");
      div.className = "card";
      div.innerHTML =
        `<strong>${event.title}</strong><br>
         ${event.date} / ${event.location}`;

      eventArea.appendChild(div);
    });
  });