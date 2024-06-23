function _compress(e, t, n) {
    if (null == e)
        return "";
    var r, o, i, a = {}, s = {}, c = "", u = "", l = "", d = 2, f = 3, p = 2, h = [], v = 0, m = 0;
    for (i = 0; i < e.length; i += 1)
        if (c = e.charAt(i),
        Object.prototype.hasOwnProperty.call(a, c) || (a[c] = f++,
            s[c] = !0),
            u = l + c,
            Object.prototype.hasOwnProperty.call(a, u))
            l = u;
        else {
            if (Object.prototype.hasOwnProperty.call(s, l)) {
                if (l.charCodeAt(0) < 256) {
                    for (r = 0; r < p; r++)
                        v <<= 1,
                            m == t - 1 ? (m = 0,
                                h.push(n(v)),
                                v = 0) : m++;
                    for (o = l.charCodeAt(0),
                             r = 0; r < 8; r++)
                        v = v << 1 | 1 & o,
                            m == t - 1 ? (m = 0,
                                h.push(n(v)),
                                v = 0) : m++,
                            o >>= 1
                } else {
                    for (o = 1,
                             r = 0; r < p; r++)
                        v = v << 1 | o,
                            m == t - 1 ? (m = 0,
                                h.push(n(v)),
                                v = 0) : m++,
                            o = 0;
                    for (o = l.charCodeAt(0),
                             r = 0; r < 16; r++)
                        v = v << 1 | 1 & o,
                            m == t - 1 ? (m = 0,
                                h.push(n(v)),
                                v = 0) : m++,
                            o >>= 1
                }
                0 == --d && (d = Math.pow(2, p),
                    p++),
                    delete s[l]
            } else
                for (o = a[l],
                         r = 0; r < p; r++)
                    v = v << 1 | 1 & o,
                        m == t - 1 ? (m = 0,
                            h.push(n(v)),
                            v = 0) : m++,
                        o >>= 1;
            0 == --d && (d = Math.pow(2, p),
                p++),
                a[u] = f++,
                l = String(c)
        }
    if ("" !== l) {
        if (Object.prototype.hasOwnProperty.call(s, l)) {
            if (l.charCodeAt(0) < 256) {
                for (r = 0; r < p; r++)
                    v <<= 1,
                        m == t - 1 ? (m = 0,
                            h.push(n(v)),
                            v = 0) : m++;
                for (o = l.charCodeAt(0),
                         r = 0; r < 8; r++)
                    v = v << 1 | 1 & o,
                        m == t - 1 ? (m = 0,
                            h.push(n(v)),
                            v = 0) : m++,
                        o >>= 1
            } else {
                for (o = 1,
                         r = 0; r < p; r++)
                    v = v << 1 | o,
                        m == t - 1 ? (m = 0,
                            h.push(n(v)),
                            v = 0) : m++,
                        o = 0;
                for (o = l.charCodeAt(0),
                         r = 0; r < 16; r++)
                    v = v << 1 | 1 & o,
                        m == t - 1 ? (m = 0,
                            h.push(n(v)),
                            v = 0) : m++,
                        o >>= 1
            }
            0 == --d && (d = Math.pow(2, p),
                p++),
                delete s[l]
        } else
            for (o = a[l],
                     r = 0; r < p; r++)
                v = v << 1 | 1 & o,
                    m == t - 1 ? (m = 0,
                        h.push(n(v)),
                        v = 0) : m++,
                    o >>= 1;
        0 == --d && (d = Math.pow(2, p),
            p++)
    }
    for (o = 2,
             r = 0; r < p; r++)
        v = v << 1 | 1 & o,
            m == t - 1 ? (m = 0,
                h.push(n(v)),
                v = 0) : m++,
            o >>= 1;
    for (; ;) {
        if (v <<= 1,
        m == t - 1) {
            h.push(n(v));
            break
        }
        m++
    }
    return h.join("")
};

var n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$';

function compress(s) {
    //s= '{"5":{"p":1,"pp":5000}}'
    let res = _compress(
        s,
        6, (function (e) {
                return n.charAt(e)
            }
        ));
    return res;
}

function _decompress(t, n, r) {
    var o, i, a, s, c, u, l, d = [], f = 4, p = 4, h = 3, v = "", m = [], g = {
        val: r(0),
        position: n,
        index: 1
    };
    for (o = 0; o < 3; o += 1)
        d[o] = o;
    for (a = 0,
             c = Math.pow(2, 2),
             u = 1; u != c;)
        s = g.val & g.position,
            g.position >>= 1,
        0 == g.position && (g.position = n,
            g.val = r(g.index++)),
            a |= (s > 0 ? 1 : 0) * u,
            u <<= 1;
    switch (a) {
        case 0:
            for (a = 0,
                     c = Math.pow(2, 8),
                     u = 1; u != c;)
                s = g.val & g.position,
                    g.position >>= 1,
                0 == g.position && (g.position = n,
                    g.val = r(g.index++)),
                    a |= (s > 0 ? 1 : 0) * u,
                    u <<= 1;
            l = e(a);
            break;
        case 1:
            for (a = 0,
                     c = Math.pow(2, 16),
                     u = 1; u != c;)
                s = g.val & g.position,
                    g.position >>= 1,
                0 == g.position && (g.position = n,
                    g.val = r(g.index++)),
                    a |= (s > 0 ? 1 : 0) * u,
                    u <<= 1;
            l = e(a);
            break;
        case 2:
            return ""
    }
    for (d[3] = l,
             i = l,
             m.push(l); ;) {
        if (g.index > t)
            return "";
        for (a = 0,
                 c = Math.pow(2, h),
                 u = 1; u != c;)
            s = g.val & g.position,
                g.position >>= 1,
            0 == g.position && (g.position = n,
                g.val = r(g.index++)),
                a |= (s > 0 ? 1 : 0) * u,
                u <<= 1;
        switch (l = a) {
            case 0:
                for (a = 0,
                         c = Math.pow(2, 8),
                         u = 1; u != c;)
                    s = g.val & g.position,
                        g.position >>= 1,
                    0 == g.position && (g.position = n,
                        g.val = r(g.index++)),
                        a |= (s > 0 ? 1 : 0) * u,
                        u <<= 1;
                d[p++] = e(a),
                    l = p - 1,
                    f--;
                break;
            case 1:
                for (a = 0,
                         c = Math.pow(2, 16),
                         u = 1; u != c;)
                    s = g.val & g.position,
                        g.position >>= 1,
                    0 == g.position && (g.position = n,
                        g.val = r(g.index++)),
                        a |= (s > 0 ? 1 : 0) * u,
                        u <<= 1;
                d[p++] = e(a),
                    l = p - 1,
                    f--;
                break;
            case 2:
                return m.join("")
        }
        if (0 == f && (f = Math.pow(2, h),
            h++),
            d[l])
            v = d[l];
        else {
            if (l !== p)
                return null;
            v = i + i.charAt(0)
        }
        m.push(v),
            d[p++] = i + v.charAt(0),
            i = v,
        0 == --f && (f = Math.pow(2, h),
            h++)
    }
}


var e = String.fromCharCode
    , t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    , n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$"
    , r = {};


function o(e, t) {
    if (!r[e]) {
        r[e] = {};
        for (var n = 0; n < e.length; n++)
            r[e][e.charAt(n)] = n
    }
    return r[e][t]
}


function decompressFromEncodedURIComponent(e) {
    return (e = e.replace(/ /g, "+"),
        _decompress(e.length, 32, (function (t) {
                return o(n, e.charAt(t))
            }
        )))
}


console.log(decompressFromEncodedURIComponent('N4IgrCBcoA5QTAGhDOl5gL6aA'));
console.log(compress('{"5":{"p":1,"pp":100}}'));