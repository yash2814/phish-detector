function toggleTab(id) {
  const contents = document.querySelectorAll('.content');
  const tabs = document.querySelectorAll('.tab');

  contents.forEach(c => c.classList.remove('show'));
  tabs.forEach(t => t.classList.remove('active-tab'));

  document.getElementById(id).classList.add('show');
  event.currentTarget.classList.add('active-tab');
}

function checkEmail() {
  const text = document.getElementById("emailInput").value.toLowerCase();
  const resultDiv = document.getElementById("result");

  if (text.includes("password") || text.includes("urgent") || text.includes("click here")) {
    resultDiv.innerHTML = "<p style='color:red;font-weight:bold;'>⚠️ This email looks like a phishing attempt!</p>";
  } else {
    resultDiv.innerHTML = "<p style='color:green;font-weight:bold;'>✅ This email looks safe.</p>";
  }
}
