const eventArea = document.getElementById("event-list");

if (eventArea) {
  fetch("data/events.json")
    .then(response => {
      if (!response.ok) throw new Error("イベント情報の取得に失敗しました");
      return response.json();
    })
    .then(events => {
      // Compare calendar dates in Japan, independently of the visitor's timezone.
      const parts = new Intl.DateTimeFormat("en-US", {
        timeZone: "Asia/Tokyo", year: "numeric", month: "2-digit", day: "2-digit"
      }).formatToParts(new Date());
      const part = type => parts.find(item => item.type === type).value;
      const today = `${part("year")}-${part("month")}-${part("day")}`;
      const upcoming = events.filter(event =>
        typeof event.date === "string" &&
        /^\d{4}-\d{2}-\d{2}$/.test(event.date) && event.date >= today
      ).sort((a, b) => a.date.localeCompare(b.date));
      eventArea.replaceChildren();
      if (!upcoming.length) {
        eventArea.textContent = "現在掲載中のイベントはありません。";
        return;
      }
      upcoming.forEach(event => {
        const card = document.createElement("div");
        card.className = "event-card";
        const title = document.createElement("strong");
        title.textContent = event.title;
        const details = document.createElement("p");
        details.textContent = `${event.date} / ${event.location}`;
        card.append(title, details);
        eventArea.appendChild(card);
      });
    })
    .catch(() => {
      eventArea.textContent = "イベント情報を読み込めませんでした。時間をおいて再度お試しください。";
    });
}
