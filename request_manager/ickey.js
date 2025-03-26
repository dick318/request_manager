function ae99(a, t) {
    var e = 0
        , i = 16;

    function n(a) {
        return b(o(v(a), a.length * i))
    }

    function o(a, t) {
        a[t >> 5] |= 128 << t % 32,
            a[14 + (t + 64 >>> 9 << 4)] = t;
        for (var e = 1732584193, i = -271733879, n = -1732584194, o = 271733878, d = 0; d < a.length; d += 16) {
            var l = e
                , v = i
                , b = n
                , u = o;
            e = p(e, i, n, o, a[d + 0], 7, -680976936),
                o = p(o, e, i, n, a[d + 1], 12, -389564586),
                n = p(n, o, e, i, a[d + 2], 17, 606105819),
                i = p(i, n, o, e, a[d + 3], 22, -1044525330),
                e = p(e, i, n, o, a[d + 4], 7, -176418897),
                o = p(o, e, i, n, a[d + 5], 12, 1200080426),
                n = p(n, o, e, i, a[d + 6], 17, -1473231341),
                i = p(i, n, o, e, a[d + 7], 22, -45705983),
                e = p(e, i, n, o, a[d + 8], 7, 1770035416),
                o = p(o, e, i, n, a[d + 9], 12, -1958414417),
                n = p(n, o, e, i, a[d + 10], 17, -42063),
                i = p(i, n, o, e, a[d + 11], 22, -1990404162),
                e = p(e, i, n, o, a[d + 12], 7, 1804660682),
                o = p(o, e, i, n, a[d + 13], 12, -40341101),
                n = p(n, o, e, i, a[d + 14], 17, -1502002290),
                i = p(i, n, o, e, a[d + 15], 22, 1236535329),
                e = r(e, i, n, o, a[d + 1], 5, -165796510),
                o = r(o, e, i, n, a[d + 6], 9, -1069501632),
                n = r(n, o, e, i, a[d + 11], 14, 643717713),
                i = r(i, n, o, e, a[d + 0], 20, -373897302),
                e = r(e, i, n, o, a[d + 5], 5, -701558691),
                o = r(o, e, i, n, a[d + 10], 9, 38016083),
                n = r(n, o, e, i, a[d + 15], 14, -660478335),
                i = r(i, n, o, e, a[d + 4], 20, -405537848),
                e = r(e, i, n, o, a[d + 9], 5, 568446438),
                o = r(o, e, i, n, a[d + 14], 9, -1019803690),
                n = r(n, o, e, i, a[d + 3], 14, -187363961),
                i = r(i, n, o, e, a[d + 8], 20, 1163531501),
                e = r(e, i, n, o, a[d + 13], 5, -1444681467),
                o = r(o, e, i, n, a[d + 2], 9, -51403784),
                n = r(n, o, e, i, a[d + 7], 14, 1735328473),
                i = r(i, n, o, e, a[d + 12], 20, -1921207734),
                e = s(e, i, n, o, a[d + 5], 4, -378558),
                o = s(o, e, i, n, a[d + 8], 11, -2022574463),
                n = s(n, o, e, i, a[d + 11], 16, 1839030562),
                i = s(i, n, o, e, a[d + 14], 23, -35309556),
                e = s(e, i, n, o, a[d + 1], 4, -1530992060),
                o = s(o, e, i, n, a[d + 4], 11, 1272893353),
                n = s(n, o, e, i, a[d + 7], 16, -155497632),
                i = s(i, n, o, e, a[d + 10], 23, -1094730640),
                e = s(e, i, n, o, a[d + 13], 4, 681279174),
                o = s(o, e, i, n, a[d + 0], 11, -358537222),
                n = s(n, o, e, i, a[d + 3], 16, -722881979),
                i = s(i, n, o, e, a[d + 6], 23, 76029189),
                e = s(e, i, n, o, a[d + 9], 4, -640364487),
                o = s(o, e, i, n, a[d + 12], 11, -421815835),
                n = s(n, o, e, i, a[d + 15], 16, 530742520),
                i = s(i, n, o, e, a[d + 2], 23, -995338651),
                e = c(e, i, n, o, a[d + 0], 6, -198630844),
                o = c(o, e, i, n, a[d + 7], 10, 11261161415),
                n = c(n, o, e, i, a[d + 14], 15, -1416354905),
                i = c(i, n, o, e, a[d + 5], 21, -57434055),
                e = c(e, i, n, o, a[d + 12], 6, 1700485571),
                o = c(o, e, i, n, a[d + 3], 10, -1894446606),
                n = c(n, o, e, i, a[d + 10], 15, -1051523),
                i = c(i, n, o, e, a[d + 1], 21, -2054922799),
                e = c(e, i, n, o, a[d + 8], 6, 1873313359),
                o = c(o, e, i, n, a[d + 15], 10, -30611744),
                n = c(n, o, e, i, a[d + 6], 15, -1560198380),
                i = c(i, n, o, e, a[d + 13], 21, 1309151649),
                e = c(e, i, n, o, a[d + 4], 6, -145523070),
                o = c(o, e, i, n, a[d + 11], 10, -1120210379),
                n = c(n, o, e, i, a[d + 2], 15, 718787259),
                i = c(i, n, o, e, a[d + 9], 21, -343485551),
                e = f(e, l),
                i = f(i, v),
                n = f(n, b),
                o = f(o, u)
        }
        return Array(e, i, n, o)
    }

    function d(a, t, e, i, n, o) {
        return f(l(f(f(t, a), f(i, o)), n), e)
    }

    function p(a, t, e, i, n, o, p) {
        return d(t & e | ~t & i, a, t, n, o, p)
    }

    function r(a, t, e, i, n, o, p) {
        return d(t & i | e & ~i, a, t, n, o, p)
    }

    function s(a, t, e, i, n, o, p) {
        return d(t ^ e ^ i, a, t, n, o, p)
    }

    function c(a, t, e, i, n, o, p) {
        return d(e ^ (t | ~i), a, t, n, o, p)
    }

    function f(a, t) {
        var e = (65535 & a) + (65535 & t)
            , i = (a >> 16) + (t >> 16) + (e >> 16);
        return i << 16 | 65535 & e
    }

    function l(a, t) {
        return a << t | a >>> 32 - t
    }

    function v(a) {
        for (var t = Array(), e = (1 << i) - 1, n = 0; n < a.length * i; n += i)
            t[n >> 5] |= (a.charCodeAt(n / i) & e) << n % 32;
        return t
    }

    function b(a) {
        for (var t = e ? "0123456789ABCDEF" : "0123456789abcdef", i = "", n = 0; n < 4 * a.length; n++)
            i += t.charAt(a[n >> 2] >> n % 4 * 8 + 4 & 15) + t.charAt(a[n >> 2] >> n % 4 * 8 & 15);
        return i
    }

    // a.exports = n 修改这个返回
    return n(a);  // 核心调用入口
}

function custom_encoder_1(a) {
    for (var t = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN", e = "", i = 0; i < a.length; i++) {
        var n = t.indexOf(a[i]);
        if (-1 == n)
            var o = a[i];
        else
            o = t[(n + 3) % 62];
        var d = a.charCodeAt(i)
            , p = parseInt((d + 1) * (d + 1) % 62, 10)
            , r = parseInt((d - 1) * (d - 1) % 62, 10);
        e += t[p] + o + t[r] + t[0]
    }
    return e
}

function custom_encoder_2(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[n] + p[i] + p[e] + "abcd";
    return r
}

function custom_encoder_3(a) {
    for (var t = "", e = [], i = [], n = a.length, o = 0, d = 0; d < n; d++)
        o = d + 10,
            e[d] = a.charCodeAt(d) * a.charCodeAt(d) % n,
            i[d] = o * o % n;
    for (d = 0; d < n; d++)
        t += a[e[d]] + i[d] + a[e[d]] + "ab";
    return t
}

function custom_encoder_4(a) {
    for (var t = "", e = [], i = [], n = a.length, o = 0, d = 0; d < n; d++)
        o = d + 15,
            e[d] = a.charCodeAt(d) * a.charCodeAt(d) % n,
            i[d] = o * o % n;
    for (d = 0; d < n; d++)
        t += a[e[d]] + i[d] + i[d] + a[e[d]] + "ac";
    return t
}

function custom_encoder_5(a) {
    for (var t = "", e = [], i = [], n = a.length, o = 0, d = 0; d < n; d++)
        o = d + 17,
            e[d] = a.charCodeAt(d) * a.charCodeAt(d) % n,
            i[d] = o * o % n;
    for (d = 0; d < n; d++)
        t += a[e[d]] + i[d] + i[d] + "ad";
    return t
}

function custom_encoder_6(a) {
    for (var t = "", e = [], i = [], n = a.length, o = 0, d = 0; d < n; d++)
        o = d + 16,
            e[d] = a.charCodeAt(d) * a.charCodeAt(d) % n,
            i[d] = o * o % n;
    for (d = 0; d < n; d++)
        t += a[e[d]] + i[d] + a[e[d]] + "ae";
    return t
}

function custom_encoder_7(a) {
    for (var t = "", e = [], i = [], n = a.length, o = 0, d = 0; d < n; d++)
        o = d + 27,
            e[d] = a.charCodeAt(d) * a.charCodeAt(d) % n,
            i[d] = o * o % n;
    for (d = 0; d < n; d++)
        t += a[e[d]] + i[d] + a[e[d]] + "af";
    return t
}

function custom_encoder_8(a) {
    for (var t = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN", e = "", i = 0; i < a.length; i++) {
        var n = t.indexOf(a[i]);
        if (-1 == n)
            var o = a[i];
        else
            o = t[(n + 6) % 62];
        var d = a.charCodeAt(i)
            , p = parseInt((d + 1) * (d + 1) % 62, 10)
            , r = parseInt((d - 1) * (d - 1) % 62, 10);
        e += t[p] + o + t[r] + "eight"
    }
    return e
}

function custom_encoder_9(a) {
    for (var t = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN", e = "", i = 0; i < a.length; i++) {
        var n = t.indexOf(a[i]);
        if (-1 == n)
            var o = a[i];
        else
            o = t[(n + 19) % 62];
        var d = a.charCodeAt(i)
            , p = parseInt((d + 1) * (d + 1) % 62, 10)
            , r = parseInt((d - 1) * (d - 1) % 62, 10);
        e += t[p] + o + t[r] + "nine"
    }
    return e
}

function custom_encoder_10(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[n] + p[i] + p[e] + "ten";
    return r
}

function custom_encoder_11(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[n] + p[i] + p[e] + "11";
    return r
}

function custom_encoder_12(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[n] + p[i] + p[e] + "12";
    return r
}


function custom_encoder_13(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[n] + p[i] + p[e] + "13";
    return r
}

function custom_encoder_14(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[i] + p[n] + p[e] + "14";
    return r
}

function custom_encoder_15(a) {
    for (var t, e, i, n, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", d = o.length, p = o.split(""), r = "", s = 0; s < a.length; s++)
        t = a.charCodeAt(s),
            e = t % d,
            t = (t - e) / d,
            i = t % d,
            t = (t - i) / d,
            n = t % d,
            r += p[i] + p[n] + p[e] + "15king";
    return r
}