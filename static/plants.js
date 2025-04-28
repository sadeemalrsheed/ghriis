// plants.js

// Function to show the selected region and scroll smoothly to it
function showRegion(regionId) {
  // Hide all plant regions
  document.querySelectorAll('.plant-region').forEach(section => {
    section.classList.add('hidden');
  });

  // Show the selected region
  const region = document.getElementById(regionId);
  if (region) {
    region.classList.remove('hidden'); // Unhide the selected region
    region.scrollIntoView({ behavior: 'smooth' }); // Smooth scroll to the selected region
  }
}

// Optional: Smooth scroll for internal navigation (if you have anchor links)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});
