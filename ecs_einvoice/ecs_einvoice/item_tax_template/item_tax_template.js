frappe.ui.form.on("Item Tax Template", "tax_type", function(frm) {
    if (cur_frm.doc.tax_type == "Value added tax - ضريبه القيمه المضافه") {
        cur_frm.set_value('tax_code', 'T1');
    }
    if (cur_frm.doc.tax_type == "Table tax (percentage) - ضريبه الجدول (نسبيه)") {
        cur_frm.set_value('tax_code', 'T2');
    }
    if (cur_frm.doc.tax_type == "Table tax (Fixed Amount) - ضريبه الجدول (النوعية)") {
        cur_frm.set_value('tax_code', 'T3');
    }
    if (cur_frm.doc.tax_type == "Withholding tax (WHT) - الخصم تحت حساب الضريبه") {
        cur_frm.set_value('tax_code', 'T4');
    }
    if (cur_frm.doc.tax_type == "Stamping tax (percentage) - ضريبه الدمغه (نسبيه)") {
        cur_frm.set_value('tax_code', 'T5');
    }
    if (cur_frm.doc.tax_type == "Stamping Tax (amount) - ضريبه الدمغه (قطعيه بمقدار ثابت)") {
        cur_frm.set_value('tax_code', 'T6');
    }
    if (cur_frm.doc.tax_type == "Entertainment tax - ضريبة الملاهى") {
        cur_frm.set_value('tax_code', 'T7');
    }
    if (cur_frm.doc.tax_type == "Resource development fee - رسم تنميه الموارد") {
        cur_frm.set_value('tax_code', 'T8');
    }
    if (cur_frm.doc.tax_type == "Service charges - رسم خدمة") {
        cur_frm.set_value('tax_code', 'T9');
    }
    if (cur_frm.doc.tax_type == "Municipality Fees - رسم المحليات") {
        cur_frm.set_value('tax_code', 'T10');
    }
    if (cur_frm.doc.tax_type == "Medical insurance fee - رسم التامين الصحى") {
        cur_frm.set_value('tax_code', 'T11');
    }
    if (cur_frm.doc.tax_type == "Other fees - رسوم أخرى") {
        cur_frm.set_value('tax_code', 'T12');
    }
});