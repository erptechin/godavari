if (document.getElementById("toggleForm")) {
    document.getElementById("toggleForm").addEventListener("click", function () {
        document.getElementById("toggleDiv").classList.toggle("hidden");
        const img = document.getElementById("toggleImage");
        img.classList.toggle("rotate-90");
        img.classList.toggle("-rotate-90");
    });
}