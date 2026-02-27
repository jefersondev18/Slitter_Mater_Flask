document.getElementById("btnExportarExcel").addEventListener("click", () => {
    const log = document.getElementById("logMsg");
    const status = document.getElementById("statusExport");

    log.innerText = "Processando exportação...";
    status.innerText = "Exportando arquivo Excel...";

    fetch("/exportar_excel")
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro na exportação");
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "dados_sistema.xlsx";
            document.body.appendChild(a);
            a.click();
            a.remove();

            log.innerText = "Exportação concluída com sucesso.";
            status.innerText = "Última exportação realizada com sucesso.";
        })
        .catch(err => {
            log.innerText = "Erro ao exportar arquivo.";
            status.innerText = "Falha na exportação.";
        });
});