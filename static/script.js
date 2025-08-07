document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("churnForm");
  const spinner = document.getElementById("spinner");
  const resultDiv = document.getElementById("result");
  const toast = document.getElementById("toast");
  const ctx = document.getElementById("probChart").getContext("2d");
  const chartContainer = document.querySelector(".graph-container");
  let myChart;

  const showToast = (message) => {
    toast.textContent = message;
    toast.style.display = "block";
    setTimeout(() => {
      toast.style.display = "none";
    }, 3000);
  };

  document.getElementById("darkToggle").onclick = () => {
    document.body.classList.toggle("dark");
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    spinner.style.display = "block";
    resultDiv.textContent = "";
    chartContainer.style.display = "none";

    const data = {
      gender: document.getElementById("gender").value,
      SeniorCitizen: document.getElementById("SeniorCitizen").value,
      MonthlyCharges: parseFloat(document.getElementById("MonthlyCharges").value),
      TotalCharges: parseFloat(document.getElementById("TotalCharges").value)
    };

    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();
      const churn = result.churn;
      const probs = result.probabilities;

      spinner.style.display = "none";
      resultDiv.textContent = churn ? "❌ Likely to Churn" : "✅ Not Likely to Churn";
      showToast("Prediction Complete");

      if (probs) {
        chartContainer.style.display = "block";
        if (myChart) myChart.destroy();
        myChart = new Chart(ctx, {
          type: "bar",
          data: {
            labels: ["No Churn", "Churn"],
            datasets: [{
              label: "Probability",
              data: probs,
              backgroundColor: ["#28a745", "#dc3545"]
            }]
          },
          options: {
            responsive: true,
            plugins: {
              legend: { display: false }
            },
            scales: {
              y: {
                beginAtZero: true,
                max: 1
              }
            }
          }
        });
      }
    } catch (err) {
      spinner.style.display = "none";
      showToast("Prediction failed.");
      console.error(err);
    }
  });
});
