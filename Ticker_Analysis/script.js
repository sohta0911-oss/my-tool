function execute(type) {
    // 入力された文字をバケツ(val)に入れる。trim()で余計な空白を削除
    const val = document.getElementById('ticker').value.trim();
    if (!val) return; // 空っぽなら何もしない

    // 日本株かどうかの判定 (数字4桁 または 3桁+英字)
    const isJapan = /^\d{4}$/.test(val) || /^\d{3}[A-Z]$/i.test(val);
    const code = val.toUpperCase(); // 全文字を大文字にする
    let url = "";

    // 条件分岐：日本株の場合
    if (isJapan) {
        if (type === 'summary') url = `https://www.nikkei.com/nkd/company/?scode=${code}`;
        if (type === 'tv') url = `https://jp.tradingview.com/chart/?symbol=TSE:${code}`;
        if (type === 'finance') url = `https://finance.yahoo.co.jp/quote/${code}.T`;
    }
    // 条件分岐：米国株などの場合
    else {
        if (type === 'summary') url = `https://finviz.com/quote.ashx?t=${code}`;
        if (type === 'tv') url = `https://jp.tradingview.com/chart/?symbol=${code}`;
        if (type === 'finance') url = `https://finance.yahoo.co.jp/quote/${code}`;
    }

    // 作成したURLを新しいタブで開く
    if (url) window.open(url, '_blank');
}