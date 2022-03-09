if (!doc.__islocal && doc.status === 'Aberto') {
    cur_frm.add_custom_button('Efetuar Baixa', function () {
        frappe.confirm('Deseja realmente efetuar a Baixa de Registro?',
            function () {
                frappe.call({
                    "method": "frappe.client.get",
                    args: {
                        doctype: "Conta a Receber",
                        name: "btn_run_pgto"
                    },
                    callback: function (data) {
                        frappe.show_alert('Baixa Efetuada com Sucesso');
                    }
                })
            },
            function () {
                window.close();
            }
        )
    }).addClass("btn-primary");
}
