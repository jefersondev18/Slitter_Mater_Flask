document.addEventListener("DOMContentLoaded", function () {

    const refreshBtn = document.querySelector(".btn-refresh");

    refreshBtn.addEventListener("click", () => {
        console.log("Atualizar dados...");
        // futuramente: fetch() para backend Flask
    });

});