const Discord = require("discord.js");
const client = new Discord.Client();

client.on("ready", () => {
  console.log("I am ready!");
});

client.on("message", (message) => {
  if (message.content.startsWith("ping")) {
    message.channel.send("pong!");
  }
});

client.login("NDk0Mjk0NDE3MDI5NzI2MjA4.Dox1lg.D450Ap3VEMxYRjMamyXGVRQyYT4");

{
  "name": "CommandBot",
  "version": "2.0.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "abbrev": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz",
      "integrity": "sha512-nne9/IiQ/hzIhY6pdDnbBtz7DjPTKrY00P/zvPSm5pOFkl6xuGrGnXn/VtTNNfNtAfZ9/1RtehkszU9qcTii0Q==",
      "dev": true
    },
    "ansi-align": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ansi-align/-/ansi-align-2.0.0.tgz",
      "integrity": "sha1-w2rsy6VjuJzrVW82kPCx2eNUf38=",
      "dev": true,
      "requires": {
        "string-width": "2.1.1"
      }
    },
    "ansi-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz",
      "integrity": "sha1-7QMXwyIGT3lGbAKWa922Bas32Zg=",
      "dev": true
    },
    "ansi-styles": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.0.tgz",
      "integrity": "sha512-NnSOmMEYtVR2JVMIGTzynRkkaxtiq1xnFBcdQD/DnNCYPoEPsVJhM98BDyaoNOQIi7p4okdi3E27eN7GQbsUug==",
      "dev": true,
      "requires": {
        "color-convert": "1.9.1"
      }
    },
    "anymatch": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-1.3.2.tgz",
      "integrity": "sha512-0XNayC8lTHQ2OI8aljNCN3sSx6hsr/1+rlcDAotXJR7C1oZZHCNsfpbKwMjRA3Uqb5tF1Rae2oloTr4xpq+WjA==",
      "dev": true,
      "requires": {
        "micromatch": "2.3.11",
        "normalize-path": "2.1.1"
      }
    },
    "arr-diff": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz",
      "integrity": "sha1-jzuCf5Vai9ZpaX5KQlasPOrjVs8=",
      "dev": true,
      "requires": {
        "arr-flatten": "1.1.0"
      }
    },
    "arr-flatten": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz",
      "integrity": "sha512-L3hKV5R/p5o81R7O02IGnwpDmkp6E982XhtbuwSe3O4qOtMMMtodicASA1Cny2U+aCXcNpml+m4dPsvsJ3jatg==",
      "dev": true
    },
    "array-unique": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz",
      "integrity": "sha1-odl8yvy8JiXMcPrc6zalDFiwGlM=",
      "dev": true
    },
    "async-each": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz",
      "integrity": "sha1-GdOGodntxufByF04iu28xW0zYC0=",
      "dev": true
    },
    "async-limiter": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/async-limiter/-/async-limiter-1.0.0.tgz",
      "integrity": "sha512-jp/uFnooOiO+L211eZOoSyzpOITMXx1rBITauYykG3BRYPu8h0UcxsPNB04RR5vo4Tyz3+ay17tR6JVf9qzYWg=="
    },
    "balanced-match": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz",
      "integrity": "sha1-ibTRmasr7kneFk6gK4nORi1xt2c=",
      "dev": true
    },
    "binary-extensions": {
      "version": "1.11.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-1.11.0.tgz",
      "integrity": "sha1-RqoXUftqL5PuXmibsQh9SxTGwgU=",
      "dev": true
    },
    "boxen": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/boxen/-/boxen-1.2.2.tgz",
      "integrity": "sha1-Px1AMsMP/qnUsCwyLq8up0HcvOU=",
      "dev": true,
      "requires": {
        "ansi-align": "2.0.0",
        "camelcase": "4.1.0",
        "chalk": "2.3.0",
        "cli-boxes": "1.0.0",
        "string-width": "2.1.1",
        "term-size": "1.2.0",
        "widest-line": "1.0.0"
      }
    },
    "brace-expansion": {
      "version": "1.1.8",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.8.tgz",
      "integrity": "sha1-wHshHHyVLsH479Uad+8NHTmQopI=",
      "dev": true,
      "requires": {
        "balanced-match": "1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "braces": {
      "version": "1.8.5",
      "resolved": "https://registry.npmjs.org/braces/-/braces-1.8.5.tgz",
      "integrity": "sha1-uneWLhLf+WnWt2cR6RS3N4V79qc=",
      "dev": true,
      "requires": {
        "expand-range": "1.8.2",
        "preserve": "0.2.0",
        "repeat-element": "1.1.2"
      }
    },
    "camelcase": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz",
      "integrity": "sha1-1UVjW+HjPFQmScaRc+Xeas+uNN0=",
      "dev": true
    },
    "capture-stack-trace": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/capture-stack-trace/-/capture-stack-trace-1.0.0.tgz",
      "integrity": "sha1-Sm+gc5nCa7pH8LJJa00PtAjFVQ0=",
      "dev": true
    },
    "chalk": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.3.0.tgz",
      "integrity": "sha512-Az5zJR2CBujap2rqXGaJKaPHyJ0IrUimvYNX+ncCy8PJP4ltOGTrHUIo097ZaL2zMeKYpiCdqDvS6zdrTFok3Q==",
      "dev": true,
      "requires": {
        "ansi-styles": "3.2.0",
        "escape-string-regexp": "1.0.5",
        "supports-color": "4.5.0"
      }
    },
    "chokidar": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-1.7.0.tgz",
      "integrity": "sha1-eY5ol3gVHIB2tLNg5e3SjNortGg=",
      "dev": true,
      "requires": {
        "anymatch": "1.3.2",
        "async-each": "1.0.1",
        "glob-parent": "2.0.0",
        "inherits": "2.0.3",
        "is-binary-path": "1.0.1",
        "is-glob": "2.0.1",
        "path-is-absolute": "1.0.1",
        "readdirp": "2.1.0"
      }
    },
    "cli-boxes": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/cli-boxes/-/cli-boxes-1.0.0.tgz",
      "integrity": "sha1-T6kXw+WclKAEzWH47lCdplFocUM=",
      "dev": true
    },
    "code-point-at": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz",
      "integrity": "sha1-DQcLTQQ6W+ozovGkDi7bPZpMz3c=",
      "dev": true
    },
    "color-convert": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-1.9.1.tgz",
      "integrity": "sha512-mjGanIiwQJskCC18rPR6OmrZ6fm2Lc7PeGFYwCmy5J34wC6F1PzdGL6xeMfmgicfYcNLGuVFA3WzXtIDCQSZxQ==",
      "dev": true,
      "requires": {
        "color-name": "1.1.3"
      }
    },
    "color-name": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz",
      "integrity": "sha1-p9BVi9icQveV3UIyj3QIMcpTvCU=",
      "dev": true
    },
    "concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha1-2Klr13/Wjfd5OnMDajug1UBdR3s=",
      "dev": true
    },
    "configstore": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/configstore/-/configstore-3.1.1.tgz",
      "integrity": "sha512-5oNkD/L++l0O6xGXxb1EWS7SivtjfGQlRyxJsYgE0Z495/L81e2h4/d3r969hoPXuFItzNOKMtsXgYG4c7dYvw==",
      "dev": true,
      "requires": {
        "dot-prop": "4.2.0",
        "graceful-fs": "4.1.11",
        "make-dir": "1.1.0",
        "unique-string": "1.0.0",
        "write-file-atomic": "2.3.0",
        "xdg-basedir": "3.0.0"
      }
    },
    "core-util-is": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
      "integrity": "sha1-tf1UIgqivFq1eqtxQMlAdUUDwac=",
      "dev": true
    },
    "create-error-class": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/create-error-class/-/create-error-class-3.0.2.tgz",
      "integrity": "sha1-Br56vvlHo/FKMP1hBnHUAbyot7Y=",
      "dev": true,
      "requires": {
        "capture-stack-trace": "1.0.0"
      }
    },
    "cross-spawn": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-5.1.0.tgz",
      "integrity": "sha1-6L0O/uWPz/b4+UUQoKVUu/ojVEk=",
      "dev": true,
      "requires": {
        "lru-cache": "4.1.1",
        "shebang-command": "1.2.0",
        "which": "1.3.0"
      }
    },
    "crypto-random-string": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/crypto-random-string/-/crypto-random-string-1.0.0.tgz",
      "integrity": "sha1-ojD2T1aDEOFJgAmUB5DsmVRbyn4=",
      "dev": true
    },
    "debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "dev": true,
      "requires": {
        "ms": "2.0.0"
      }
    },
    "deep-extend": {
      "version": "0.4.2",
      "resolved": "https://registry.npmjs.org/deep-extend/-/deep-extend-0.4.2.tgz",
      "integrity": "sha1-SLaZwn4zS/ifEIkr5DL25MfTSn8=",
      "dev": true
    },
    "discord.js": {
      "version": "11.2.1",
      "resolved": "https://registry.npmjs.org/discord.js/-/discord.js-11.2.1.tgz",
      "integrity": "sha512-8Mor+IREVWHinjRd6Bu6OwRfT+ET/WEoLWMl8crFvBVcTFmaO/TSwP39C8QIGCB2YMVMYMdljjX/w17AUMemqg==",
      "requires": {
        "long": "3.2.0",
        "prism-media": "0.0.1",
        "snekfetch": "3.5.8",
        "tweetnacl": "1.0.0",
        "ws": "3.3.2"
      }
    },
    "dot-prop": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/dot-prop/-/dot-prop-4.2.0.tgz",
      "integrity": "sha512-tUMXrxlExSW6U2EXiiKGSBVdYgtV8qlHL+C10TsW4PURY/ic+eaysnSkwB4kA/mBlCyy/IKDJ+Lc3wbWeaXtuQ==",
      "dev": true,
      "requires": {
        "is-obj": "1.0.1"
      }
    },
    "duplexer": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/duplexer/-/duplexer-0.1.1.tgz",
      "integrity": "sha1-rOb/gIwc5mtX0ev5eXessCM0z8E=",
      "dev": true
    },
    "duplexer3": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/duplexer3/-/duplexer3-0.1.4.tgz",
      "integrity": "sha1-7gHdHKwO08vH/b6jfcCo8c4ALOI=",
      "dev": true
    },
    "es6-promise": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/es6-promise/-/es6-promise-3.3.1.tgz",
      "integrity": "sha1-oIzd6EzNvzTQJ6FFG8kdS80ophM=",
      "dev": true
    },
    "escape-string-regexp": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz",
      "integrity": "sha1-G2HAViGQqN/2rjuyzwIAyhMLhtQ=",
      "dev": true
    },
    "event-stream": {
      "version": "3.3.4",
      "resolved": "https://registry.npmjs.org/event-stream/-/event-stream-3.3.4.tgz",
      "integrity": "sha1-SrTJoPWlTbkzi0w02Gv86PSzVXE=",
      "dev": true,
      "requires": {
        "duplexer": "0.1.1",
        "from": "0.1.7",
        "map-stream": "0.1.0",
        "pause-stream": "0.0.11",
        "split": "0.3.3",
        "stream-combiner": "0.0.4",
        "through": "2.3.8"
      }
    },
    "execa": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/execa/-/execa-0.7.0.tgz",
      "integrity": "sha1-lEvs00zEHuMqY6n68nrVpl/Fl3c=",
      "dev": true,
      "requires": {
        "cross-spawn": "5.1.0",
        "get-stream": "3.0.0",
        "is-stream": "1.1.0",
        "npm-run-path": "2.0.2",
        "p-finally": "1.0.0",
        "signal-exit": "3.0.2",
        "strip-eof": "1.0.0"
      }
    },
    "expand-brackets": {
      "version": "0.1.5",
      "resolved": "https://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz",
      "integrity": "sha1-3wcoTjQqgHzXM6xa9yQR5YHRF3s=",
      "dev": true,
      "requires": {
        "is-posix-bracket": "0.1.1"
      }
    },
    "expand-range": {
      "version": "1.8.2",
      "resolved": "https://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz",
      "integrity": "sha1-opnv/TNf4nIeuujiV+x5ZE/IUzc=",
      "dev": true,
      "requires": {
        "fill-range": "2.2.3"
      }
    },
    "extglob": {
      "version": "0.3.2",
      "resolved": "https://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz",
      "integrity": "sha1-Lhj/PS9JqydlzskCPwEdqo2DSaE=",
      "dev": true,
      "requires": {
        "is-extglob": "1.0.0"
      }
    },
    "filename-regex": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz",
      "integrity": "sha1-wcS5vuPglyXdsQa3XB4wH+LxiyY=",
      "dev": true
    },
    "fill-range": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-2.2.3.tgz",
      "integrity": "sha1-ULd9/X5Gm8dJJHCWNpn+eoSFpyM=",
      "dev": true,
      "requires": {
        "is-number": "2.1.0",
        "isobject": "2.1.0",
        "randomatic": "1.1.7",
        "repeat-element": "1.1.2",
        "repeat-string": "1.6.1"
      }
    },
    "for-in": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz",
      "integrity": "sha1-gQaNKVqBQuwKxybG4iAMMPttXoA=",
      "dev": true
    },
    "for-own": {
      "version": "0.1.5",
      "resolved": "https://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz",
      "integrity": "sha1-UmXGgaTylNq78XyVCbZ2OqhFEM4=",
      "dev": true,
      "requires": {
        "for-in": "1.0.2"
      }
    },
    "from": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/from/-/from-0.1.7.tgz",
      "integrity": "sha1-g8YK/Fi5xWmXAH7Rp2izqzA6RP4=",
      "dev": true
    },
    "get-stream": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz",
      "integrity": "sha1-jpQ9E1jcN1VQVOy+LtsFqhdO3hQ=",
      "dev": true
    },
    "glob-base": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz",
      "integrity": "sha1-27Fk9iIbHAscz4Kuoyi0l98Oo8Q=",
      "dev": true,
      "requires": {
        "glob-parent": "2.0.0",
        "is-glob": "2.0.1"
      }
    },
    "glob-parent": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz",
      "integrity": "sha1-gTg9ctsFT8zPUzbaqQLxgvbtuyg=",
      "dev": true,
      "requires": {
        "is-glob": "2.0.1"
      }
    },
    "global-dirs": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/global-dirs/-/global-dirs-0.1.1.tgz",
      "integrity": "sha1-sxnA3UYH81PzvpzKTHL8FIxJ9EU=",
      "dev": true,
      "requires": {
        "ini": "1.3.5"
      }
    },
    "got": {
      "version": "6.7.1",
      "resolved": "https://registry.npmjs.org/got/-/got-6.7.1.tgz",
      "integrity": "sha1-JAzQV4WpoY5WHcG0S0HHY+8ejbA=",
      "dev": true,
      "requires": {
        "create-error-class": "3.0.2",
        "duplexer3": "0.1.4",
        "get-stream": "3.0.0",
        "is-redirect": "1.0.0",
        "is-retry-allowed": "1.1.0",
        "is-stream": "1.1.0",
        "lowercase-keys": "1.0.0",
        "safe-buffer": "5.1.1",
        "timed-out": "4.0.1",
        "unzip-response": "2.0.1",
        "url-parse-lax": "1.0.0"
      }
    },
    "graceful-fs": {
      "version": "4.1.11",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz",
      "integrity": "sha1-Dovf5NHduIVNZOBOp8AOKgJuVlg=",
      "dev": true
    },
    "has-flag": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz",
      "integrity": "sha1-6CB68cx7MNRGzHC3NLXovhj4jVE=",
      "dev": true
    },
    "ignore-by-default": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/ignore-by-default/-/ignore-by-default-1.0.1.tgz",
      "integrity": "sha1-SMptcvbGo68Aqa1K5odr44ieKwk=",
      "dev": true
    },
    "import-lazy": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/import-lazy/-/import-lazy-2.1.0.tgz",
      "integrity": "sha1-BWmOPUXIjo1+nZLLBYTnfwlvPkM=",
      "dev": true
    },
    "imurmurhash": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz",
      "integrity": "sha1-khi5srkoojixPcT7a21XbyMUU+o=",
      "dev": true
    },
    "inherits": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
      "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4=",
      "dev": true
    },
    "ini": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/ini/-/ini-1.3.5.tgz",
      "integrity": "sha512-RZY5huIKCMRWDUqZlEi72f/lmXKMvuszcMBduliQ3nnWbx9X/ZBQO7DijMEYS9EhHBb2qacRUMtC7svLwe0lcw==",
      "dev": true
    },
    "is-binary-path": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz",
      "integrity": "sha1-dfFmQrSA8YenEcgUFh/TpKdlWJg=",
      "dev": true,
      "requires": {
        "binary-extensions": "1.11.0"
      }
    },
    "is-buffer": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz",
      "integrity": "sha512-NcdALwpXkTm5Zvvbk7owOUSvVvBKDgKP5/ewfXEznmQFfs4ZRmanOeKBTjRVjka3QFoN6XJ+9F3USqfHqTaU5w==",
      "dev": true
    },
    "is-dotfile": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz",
      "integrity": "sha1-pqLzL/0t+wT1yiXs0Pa4PPeYoeE=",
      "dev": true
    },
    "is-equal-shallow": {
      "version": "0.1.3",
      "resolved": "https://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz",
      "integrity": "sha1-IjgJj8Ih3gvPpdnqxMRdY4qhxTQ=",
      "dev": true,
      "requires": {
        "is-primitive": "2.0.0"
      }
    },
    "is-extendable": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz",
      "integrity": "sha1-YrEQ4omkcUGOPsNqYX1HLjAd/Ik=",
      "dev": true
    },
    "is-extglob": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz",
      "integrity": "sha1-rEaBd8SUNAWgkvyPKXYMb/xiBsA=",
      "dev": true
    },
    "is-fullwidth-code-point": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz",
      "integrity": "sha1-o7MKXE8ZkYMWeqq5O+764937ZU8=",
      "dev": true
    },
    "is-glob": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz",
      "integrity": "sha1-0Jb5JqPe1WAPP9/ZEZjLCIjC2GM=",
      "dev": true,
      "requires": {
        "is-extglob": "1.0.0"
      }
    },
    "is-installed-globally": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/is-installed-globally/-/is-installed-globally-0.1.0.tgz",
      "integrity": "sha1-Df2Y9akRFxbdU13aZJL2e/PSWoA=",
      "dev": true,
      "requires": {
        "global-dirs": "0.1.1",
        "is-path-inside": "1.0.0"
      }
    },
    "is-npm": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-npm/-/is-npm-1.0.0.tgz",
      "integrity": "sha1-8vtjpl5JBbQGyGBydloaTceTufQ=",
      "dev": true
    },
    "is-number": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz",
      "integrity": "sha1-Afy7s5NGOlSPL0ZszhbezknbkI8=",
      "dev": true,
      "requires": {
        "kind-of": "3.2.2"
      }
    },
    "is-obj": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/is-obj/-/is-obj-1.0.1.tgz",
      "integrity": "sha1-PkcprB9f3gJc19g6iW2rn09n2w8=",
      "dev": true
    },
    "is-path-inside": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-path-inside/-/is-path-inside-1.0.0.tgz",
      "integrity": "sha1-/AbloWg/vaE95mev9xe7wQpI838=",
      "dev": true,
      "requires": {
        "path-is-inside": "1.0.2"
      }
    },
    "is-posix-bracket": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz",
      "integrity": "sha1-MzTceXdDaOkvAW5vvAqI9c1ua8Q=",
      "dev": true
    },
    "is-primitive": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz",
      "integrity": "sha1-IHurkWOEmcB7Kt8kCkGochADRXU=",
      "dev": true
    },
    "is-redirect": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-redirect/-/is-redirect-1.0.0.tgz",
      "integrity": "sha1-HQPd7VO9jbDzDCbk+V02/HyH3CQ=",
      "dev": true
    },
    "is-retry-allowed": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-retry-allowed/-/is-retry-allowed-1.1.0.tgz",
      "integrity": "sha1-EaBgVotnM5REAz0BJaYaINVk+zQ=",
      "dev": true
    },
    "is-stream": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz",
      "integrity": "sha1-EtSj3U5o4Lec6428hBc66A2RykQ=",
      "dev": true
    },
    "isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha1-u5NdSFgsuhaMBoNJV6VKPgcSTxE=",
      "dev": true
    },
    "isexe": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
      "integrity": "sha1-6PvzdNxVb/iUehDcsFctYz8s+hA=",
      "dev": true
    },
    "isobject": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz",
      "integrity": "sha1-8GVWEJaj8dou9GJy+BXIQNh+DIk=",
      "dev": true,
      "requires": {
        "isarray": "1.0.0"
      }
    },
    "kind-of": {
      "version": "3.2.2",
      "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
      "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
      "dev": true,
      "requires": {
        "is-buffer": "1.1.6"
      }
    },
    "latest-version": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/latest-version/-/latest-version-3.1.0.tgz",
      "integrity": "sha1-ogU4P+oyKzO1rjsYq+4NwvNW7hU=",
      "dev": true,
      "requires": {
        "package-json": "4.0.1"
      }
    },
    "lodash._baseassign": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/lodash._baseassign/-/lodash._baseassign-3.2.0.tgz",
      "integrity": "sha1-jDigmVAPIVrQnlnxci/QxSv+Ck4=",
      "dev": true,
      "requires": {
        "lodash._basecopy": "3.0.1",
        "lodash.keys": "3.1.2"
      }
    },
    "lodash._basecopy": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/lodash._basecopy/-/lodash._basecopy-3.0.1.tgz",
      "integrity": "sha1-jaDmqHbPNEwK2KVIghEd08XHyjY=",
      "dev": true
    },
    "lodash._bindcallback": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/lodash._bindcallback/-/lodash._bindcallback-3.0.1.tgz",
      "integrity": "sha1-5THCdkTPi1epnhftlbNcdIeJOS4=",
      "dev": true
    },
    "lodash._createassigner": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/lodash._createassigner/-/lodash._createassigner-3.1.1.tgz",
      "integrity": "sha1-g4pbri/aymOsIt7o4Z+k5taXCxE=",
      "dev": true,
      "requires": {
        "lodash._bindcallback": "3.0.1",
        "lodash._isiterateecall": "3.0.9",
        "lodash.restparam": "3.6.1"
      }
    },
    "lodash._getnative": {
      "version": "3.9.1",
      "resolved": "https://registry.npmjs.org/lodash._getnative/-/lodash._getnative-3.9.1.tgz",
      "integrity": "sha1-VwvH3t5G1hzc3mh9ZdPuy6o6r/U=",
      "dev": true
    },
    "lodash._isiterateecall": {
      "version": "3.0.9",
      "resolved": "https://registry.npmjs.org/lodash._isiterateecall/-/lodash._isiterateecall-3.0.9.tgz",
      "integrity": "sha1-UgOte6Ql+uhCRg5pbbnPPmqsBXw=",
      "dev": true
    },
    "lodash.assign": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/lodash.assign/-/lodash.assign-3.2.0.tgz",
      "integrity": "sha1-POnwI0tLIiPilrj6CsH+6OvKZPo=",
      "dev": true,
      "requires": {
        "lodash._baseassign": "3.2.0",
        "lodash._createassigner": "3.1.1",
        "lodash.keys": "3.1.2"
      }
    },
    "lodash.defaults": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-3.1.2.tgz",
      "integrity": "sha1-xzCLGNv4vJNy1wGnNJPGEZK9Liw=",
      "dev": true,
      "requires": {
        "lodash.assign": "3.2.0",
        "lodash.restparam": "3.6.1"
      }
    },
    "lodash.isarguments": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/lodash.isarguments/-/lodash.isarguments-3.1.0.tgz",
      "integrity": "sha1-L1c9hcaiQon/AGY7SRwdM4/zRYo=",
      "dev": true
    },
    "lodash.isarray": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/lodash.isarray/-/lodash.isarray-3.0.4.tgz",
      "integrity": "sha1-eeTriMNqgSKvhvhEqpvNhRtfu1U=",
      "dev": true
    },
    "lodash.keys": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/lodash.keys/-/lodash.keys-3.1.2.tgz",
      "integrity": "sha1-TbwEcrFWvlCgsoaFXRvQsMZWCYo=",
      "dev": true,
      "requires": {
        "lodash._getnative": "3.9.1",
        "lodash.isarguments": "3.1.0",
        "lodash.isarray": "3.0.4"
      }
    },
    "lodash.restparam": {
      "version": "3.6.1",
      "resolved": "https://registry.npmjs.org/lodash.restparam/-/lodash.restparam-3.6.1.tgz",
      "integrity": "sha1-k2pOMJ7zMKdkXtQUWYbIWuWyCAU=",
      "dev": true
    },
    "long": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/long/-/long-3.2.0.tgz",
      "integrity": "sha1-2CG3E4yhy1gcFymQ7xTbIAtcR0s="
    },
    "lowercase-keys": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-1.0.0.tgz",
      "integrity": "sha1-TjNms55/VFfjXxMkvfb4jQv8cwY=",
      "dev": true
    },
    "lru-cache": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.1.tgz",
      "integrity": "sha512-q4spe4KTfsAS1SUHLO0wz8Qiyf1+vMIAgpRYioFYDMNqKfHQbg+AVDH3i4fvpl71/P1L0dBl+fQi+P37UYf0ew==",
      "dev": true,
      "requires": {
        "pseudomap": "1.0.2",
        "yallist": "2.1.2"
      }
    },
    "make-dir": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/make-dir/-/make-dir-1.1.0.tgz",
      "integrity": "sha512-0Pkui4wLJ7rxvmfUvs87skoEaxmu0hCUApF8nonzpl7q//FWp9zu8W61Scz4sd/kUiqDxvUhtoam2efDyiBzcA==",
      "dev": true,
      "requires": {
        "pify": "3.0.0"
      }
    },
    "map-stream": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/map-stream/-/map-stream-0.1.0.tgz",
      "integrity": "sha1-5WqpTEyAVaFkBKBnS3jyFffI4ZQ=",
      "dev": true
    },
    "micromatch": {
      "version": "2.3.11",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz",
      "integrity": "sha1-hmd8l9FyCzY0MdBNDRUpO9OMFWU=",
      "dev": true,
      "requires": {
        "arr-diff": "2.0.0",
        "array-unique": "0.2.1",
        "braces": "1.8.5",
        "expand-brackets": "0.1.5",
        "extglob": "0.3.2",
        "filename-regex": "2.0.1",
        "is-extglob": "1.0.0",
        "is-glob": "2.0.1",
        "kind-of": "3.2.2",
        "normalize-path": "2.1.1",
        "object.omit": "2.0.1",
        "parse-glob": "3.0.4",
        "regex-cache": "0.4.4"
      }
    },
    "minimatch": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz",
      "integrity": "sha512-yJHVQEhyqPLUTgt9B83PXu6W3rx4MvvHvSUvToogpwoGDOUQ+yDrR0HRot+yOCdCO7u4hX3pWft6kWBBcqh0UA==",
      "dev": true,
      "requires": {
        "brace-expansion": "1.1.8"
      }
    },
    "minimist": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz",
      "integrity": "sha1-o1AIsg9BOD7sH7kU9M1d95omQoQ=",
      "dev": true
    },
    "ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g=",
      "dev": true
    },
    "nodemon": {
      "version": "1.12.1",
      "resolved": "https://registry.npmjs.org/nodemon/-/nodemon-1.12.1.tgz",
      "integrity": "sha1-mWpW3EnZ8Wu/G3ik3gjxNjSzh40=",
      "dev": true,
      "requires": {
        "chokidar": "1.7.0",
        "debug": "2.6.9",
        "es6-promise": "3.3.1",
        "ignore-by-default": "1.0.1",
        "lodash.defaults": "3.1.2",
        "minimatch": "3.0.4",
        "ps-tree": "1.1.0",
        "touch": "3.1.0",
        "undefsafe": "0.0.3",
        "update-notifier": "2.3.0"
      }
    },
    "nopt": {
      "version": "1.0.10",
      "resolved": "https://registry.npmjs.org/nopt/-/nopt-1.0.10.tgz",
      "integrity": "sha1-bd0hvSoxQXuScn3Vhfim83YI6+4=",
      "dev": true,
      "requires": {
        "abbrev": "1.1.1"
      }
    },
    "normalize-path": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz",
      "integrity": "sha1-GrKLVW4Zg2Oowab35vogE3/mrtk=",
      "dev": true,
      "requires": {
        "remove-trailing-separator": "1.1.0"
      }
    },
    "npm-run-path": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz",
      "integrity": "sha1-NakjLfo11wZ7TLLd8jV7GHFTbF8=",
      "dev": true,
      "requires": {
        "path-key": "2.0.1"
      }
    },
    "number-is-nan": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz",
      "integrity": "sha1-CXtgK1NCKlIsGvuHkDGDNpQaAR0=",
      "dev": true
    },
    "object.omit": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz",
      "integrity": "sha1-Gpx0SCnznbuFjHbKNXmuKlTr0fo=",
      "dev": true,
      "requires": {
        "for-own": "0.1.5",
        "is-extendable": "0.1.1"
      }
    },
    "p-finally": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz",
      "integrity": "sha1-P7z7FbiZpEEjs0ttzBi3JDNqLK4=",
      "dev": true
    },
    "package-json": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/package-json/-/package-json-4.0.1.tgz",
      "integrity": "sha1-iGmgQBJTZhxMTKPabCEh7VVfXu0=",
      "dev": true,
      "requires": {
        "got": "6.7.1",
        "registry-auth-token": "3.3.1",
        "registry-url": "3.1.0",
        "semver": "5.4.1"
      }
    },
    "parse-glob": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz",
      "integrity": "sha1-ssN2z7EfNVE7rdFz7wu246OIORw=",
      "dev": true,
      "requires": {
        "glob-base": "0.3.0",
        "is-dotfile": "1.0.3",
        "is-extglob": "1.0.0",
        "is-glob": "2.0.1"
      }
    },
    "path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha1-F0uSaHNVNP+8es5r9TpanhtcX18=",
      "dev": true
    },
    "path-is-inside": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/path-is-inside/-/path-is-inside-1.0.2.tgz",
      "integrity": "sha1-NlQX3t5EQw0cEa9hAn+s8HS9/FM=",
      "dev": true
    },
    "path-key": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz",
      "integrity": "sha1-QRyttXTFoUDTpLGRDUDYDMn0C0A=",
      "dev": true
    },
    "pause-stream": {
      "version": "0.0.11",
      "resolved": "https://registry.npmjs.org/pause-stream/-/pause-stream-0.0.11.tgz",
      "integrity": "sha1-/lo0sMvOErWqaitAPuLnO2AvFEU=",
      "dev": true,
      "requires": {
        "through": "2.3.8"
      }
    },
    "pify": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/pify/-/pify-3.0.0.tgz",
      "integrity": "sha1-5aSs0sEB/fPZpNB/DbxNtJ3SgXY=",
      "dev": true
    },
    "prepend-http": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz",
      "integrity": "sha1-1PRWKwzjaW5BrFLQ4ALlemNdxtw=",
      "dev": true
    },
    "preserve": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz",
      "integrity": "sha1-gV7R9uvGWSb4ZbMQwHE7yzMVzks=",
      "dev": true
    },
    "prism-media": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/prism-media/-/prism-media-0.0.1.tgz",
      "integrity": "sha1-o0JcnKvVDRxsAuVDlBoRiVZnvRA="
    },
    "process-nextick-args": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz",
      "integrity": "sha1-FQ4gt1ZZCtP5EJPyWk8q2L/zC6M=",
      "dev": true
    },
    "ps-tree": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/ps-tree/-/ps-tree-1.1.0.tgz",
      "integrity": "sha1-tCGyQUDWID8e08dplrRCewjowBQ=",
      "dev": true,
      "requires": {
        "event-stream": "3.3.4"
      }
    },
    "pseudomap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz",
      "integrity": "sha1-8FKijacOYYkX7wqKw0wa5aaChrM=",
      "dev": true
    },
    "random-js": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/random-js/-/random-js-1.0.8.tgz",
      "integrity": "sha1-lo/WiabyXWwKrHZig94vaIycGQo="
    },
    "randomatic": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/randomatic/-/randomatic-1.1.7.tgz",
      "integrity": "sha512-D5JUjPyJbaJDkuAazpVnSfVkLlpeO3wDlPROTMLGKG1zMFNFRgrciKo1ltz/AzNTkqE0HzDx655QOL51N06how==",
      "dev": true,
      "requires": {
        "is-number": "3.0.0",
        "kind-of": "4.0.0"
      },
      "dependencies": {
        "is-number": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz",
          "integrity": "sha1-JP1iAaR4LPUFYcgQJ2r8fRLXEZU=",
          "dev": true,
          "requires": {
            "kind-of": "3.2.2"
          },
          "dependencies": {
            "kind-of": {
              "version": "3.2.2",
              "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
              "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
              "dev": true,
              "requires": {
                "is-buffer": "1.1.6"
              }
            }
          }
        },
        "kind-of": {
          "version": "4.0.0",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz",
          "integrity": "sha1-IIE989cSkosgc3hpGkUGb65y3Vc=",
          "dev": true,
          "requires": {
            "is-buffer": "1.1.6"
          }
        }
      }
    },
    "rc": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/rc/-/rc-1.2.2.tgz",
      "integrity": "sha1-2M6ctX6NZNnHut2YdsfDTL48cHc=",
      "dev": true,
      "requires": {
        "deep-extend": "0.4.2",
        "ini": "1.3.5",
        "minimist": "1.2.0",
        "strip-json-comments": "2.0.1"
      }
    },
    "readable-stream": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz",
      "integrity": "sha512-m+qzzcn7KUxEmd1gMbchF+Y2eIUbieUaxkWtptyHywrX0rE8QEYqPC07Vuy4Wm32/xE16NcdBctb8S0Xe/5IeQ==",
      "dev": true,
      "requires": {
        "core-util-is": "1.0.2",
        "inherits": "2.0.3",
        "isarray": "1.0.0",
        "process-nextick-args": "1.0.7",
        "safe-buffer": "5.1.1",
        "string_decoder": "1.0.3",
        "util-deprecate": "1.0.2"
      }
    },
    "readdirp": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz",
      "integrity": "sha1-TtCtBg3zBzMAxIRANz9y0cxkLXg=",
      "dev": true,
      "requires": {
        "graceful-fs": "4.1.11",
        "minimatch": "3.0.4",
        "readable-stream": "2.3.3",
        "set-immediate-shim": "1.0.1"
      }
    },
    "regex-cache": {
      "version": "0.4.4",
      "resolved": "https://registry.npmjs.org/regex-cache/-/regex-cache-0.4.4.tgz",
      "integrity": "sha512-nVIZwtCjkC9YgvWkpM55B5rBhBYRZhAaJbgcFYXXsHnbZ9UZI9nnVWYZpBlCqv9ho2eZryPnWrZGsOdPwVWXWQ==",
      "dev": true,
      "requires": {
        "is-equal-shallow": "0.1.3"
      }
    },
    "registry-auth-token": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/registry-auth-token/-/registry-auth-token-3.3.1.tgz",
      "integrity": "sha1-+w0yie4Nmtosu1KvXf5mywcNMAY=",
      "dev": true,
      "requires": {
        "rc": "1.2.2",
        "safe-buffer": "5.1.1"
      }
    },
    "registry-url": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/registry-url/-/registry-url-3.1.0.tgz",
      "integrity": "sha1-PU74cPc93h138M+aOBQyRE4XSUI=",
      "dev": true,
      "requires": {
        "rc": "1.2.2"
      }
    },
    "remove-trailing-separator": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz",
      "integrity": "sha1-wkvOKig62tW8P1jg1IJJuSN52O8=",
      "dev": true
    },
    "repeat-element": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz",
      "integrity": "sha1-7wiaF40Ug7quTZPrmLT55OEdmQo=",
      "dev": true
    },
    "repeat-string": {
      "version": "1.6.1",
      "resolved": "https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz",
      "integrity": "sha1-jcrkcOHIirwtYA//Sndihtp15jc=",
      "dev": true
    },
    "safe-buffer": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.1.tgz",
      "integrity": "sha512-kKvNJn6Mm93gAczWVJg7wH+wGYWNrDHdWvpUmHyEsgCtIwwo3bqPtV4tR5tuPaUhTOo/kvhVwd8XwwOllGYkbg=="
    },
    "semver": {
      "version": "5.4.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-5.4.1.tgz",
      "integrity": "sha512-WfG/X9+oATh81XtllIo/I8gOiY9EXRdv1cQdyykeXK17YcUW3EXUAi2To4pcH6nZtJPr7ZOpM5OMyWJZm+8Rsg==",
      "dev": true
    },
    "semver-diff": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/semver-diff/-/semver-diff-2.1.0.tgz",
      "integrity": "sha1-S7uEN8jTfksM8aaP1ybsbWRdbTY=",
      "dev": true,
      "requires": {
        "semver": "5.4.1"
      }
    },
    "set-immediate-shim": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz",
      "integrity": "sha1-SysbJ+uAip+NzEgaWOXlb1mfP2E=",
      "dev": true
    },
    "shebang-command": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz",
      "integrity": "sha1-RKrGW2lbAzmJaMOfNj/uXer98eo=",
      "dev": true,
      "requires": {
        "shebang-regex": "1.0.0"
      }
    },
    "shebang-regex": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz",
      "integrity": "sha1-2kL0l0DAtC2yypcoVxyxkMmO/qM=",
      "dev": true
    },
    "signal-exit": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz",
      "integrity": "sha1-tf3AjxKH6hF4Yo5BXiUTK3NkbG0=",
      "dev": true
    },
    "snekfetch": {
      "version": "3.5.8",
      "resolved": "https://registry.npmjs.org/snekfetch/-/snekfetch-3.5.8.tgz",
      "integrity": "sha512-osq7soqKBObV4u/WE9tGQT/m5JdqTU1PWVPcT0We3sKZ99h9QA7wSj7ZWrwEwgRbELeO5BrVCanYjDYtVYcwrQ=="
    },
    "split": {
      "version": "0.3.3",
      "resolved": "https://registry.npmjs.org/split/-/split-0.3.3.tgz",
      "integrity": "sha1-zQ7qXmOiEd//frDwkcQTPi0N0o8=",
      "dev": true,
      "requires": {
        "through": "2.3.8"
      }
    },
    "stream-combiner": {
      "version": "0.0.4",
      "resolved": "https://registry.npmjs.org/stream-combiner/-/stream-combiner-0.0.4.tgz",
      "integrity": "sha1-TV5DPBhSYd3mI8o/RMWGvPXErRQ=",
      "dev": true,
      "requires": {
        "duplexer": "0.1.1"
      }
    },
    "string_decoder": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz",
      "integrity": "sha512-4AH6Z5fzNNBcH+6XDMfA/BTt87skxqJlO0lAh3Dker5zThcAxG6mKz+iGu308UKoPPQ8Dcqx/4JhujzltRa+hQ==",
      "dev": true,
      "requires": {
        "safe-buffer": "5.1.1"
      }
    },
    "string-width": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz",
      "integrity": "sha512-nOqH59deCq9SRHlxq1Aw85Jnt4w6KvLKqWVik6oA9ZklXLNIOlqg4F2yrT1MVaTjAqvVwdfeZ7w7aCvJD7ugkw==",
      "dev": true,
      "requires": {
        "is-fullwidth-code-point": "2.0.0",
        "strip-ansi": "4.0.0"
      }
    },
    "strip-ansi": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz",
      "integrity": "sha1-qEeQIusaw2iocTibY1JixQXuNo8=",
      "dev": true,
      "requires": {
        "ansi-regex": "3.0.0"
      }
    },
    "strip-eof": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz",
      "integrity": "sha1-u0P/VZim6wXYm1n80SnJgzE2Br8=",
      "dev": true
    },
    "strip-json-comments": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz",
      "integrity": "sha1-PFMZQukIwml8DsNEhYwobHygpgo=",
      "dev": true
    },
    "supports-color": {
      "version": "4.5.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.5.0.tgz",
      "integrity": "sha1-vnoN5ITexcXN34s9WRJQRJEvY1s=",
      "dev": true,
      "requires": {
        "has-flag": "2.0.0"
      }
    },
    "term-size": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/term-size/-/term-size-1.2.0.tgz",
      "integrity": "sha1-RYuDiH8oj8Vtb/+/rSYuJmOO+mk=",
      "dev": true,
      "requires": {
        "execa": "0.7.0"
      }
    },
    "through": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/through/-/through-2.3.8.tgz",
      "integrity": "sha1-DdTJ/6q8NXlgsbckEV1+Doai4fU=",
      "dev": true
    },
    "timed-out": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/timed-out/-/timed-out-4.0.1.tgz",
      "integrity": "sha1-8y6srFoXW+ol1/q1Zas+2HQe9W8=",
      "dev": true
    },
    "touch": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/touch/-/touch-3.1.0.tgz",
      "integrity": "sha512-WBx8Uy5TLtOSRtIq+M03/sKDrXCLHxwDcquSP2c43Le03/9serjQBIztjRz6FkJez9D/hleyAXTBGLwwZUw9lA==",
      "dev": true,
      "requires": {
        "nopt": "1.0.10"
      }
    },
    "tweetnacl": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/tweetnacl/-/tweetnacl-1.0.0.tgz",
      "integrity": "sha1-cT2LgY2kIGh0C/aDhtBHnmb8ins="
    },
    "ultron": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ultron/-/ultron-1.1.1.tgz",
      "integrity": "sha512-UIEXBNeYmKptWH6z8ZnqTeS8fV74zG0/eRU9VGkpzz+LIJNs8W/zM/L+7ctCkRrgbNnnR0xxw4bKOr0cW0N0Og=="
    },
    "undefsafe": {
      "version": "0.0.3",
      "resolved": "https://registry.npmjs.org/undefsafe/-/undefsafe-0.0.3.tgz",
      "integrity": "sha1-7Mo6A+VrmvFzhbqsgSrIO5lKli8=",
      "dev": true
    },
    "unique-string": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unique-string/-/unique-string-1.0.0.tgz",
      "integrity": "sha1-nhBXzKhRq7kzmPizOuGHuZyuwRo=",
      "dev": true,
      "requires": {
        "crypto-random-string": "1.0.0"
      }
    },
    "unzip-response": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/unzip-response/-/unzip-response-2.0.1.tgz",
      "integrity": "sha1-0vD3N9FrBhXnKmk17QQhRXLVb5c=",
      "dev": true
    },
    "update-notifier": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/update-notifier/-/update-notifier-2.3.0.tgz",
      "integrity": "sha1-TognpruRUUCrCTVZ1wFOPruDdFE=",
      "dev": true,
      "requires": {
        "boxen": "1.2.2",
        "chalk": "2.3.0",
        "configstore": "3.1.1",
        "import-lazy": "2.1.0",
        "is-installed-globally": "0.1.0",
        "is-npm": "1.0.0",
        "latest-version": "3.1.0",
        "semver-diff": "2.1.0",
        "xdg-basedir": "3.0.0"
      }
    },
    "url-parse-lax": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/url-parse-lax/-/url-parse-lax-1.0.0.tgz",
      "integrity": "sha1-evjzA2Rem9eaJy56FKxovAYJ2nM=",
      "dev": true,
      "requires": {
        "prepend-http": "1.0.4"
      }
    },
    "util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha1-RQ1Nyfpw3nMnYvvS1KKJgUGaDM8=",
      "dev": true
    },
    "which": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/which/-/which-1.3.0.tgz",
      "integrity": "sha512-xcJpopdamTuY5duC/KnTTNBraPK54YwpenP4lzxU8H91GudWpFv38u0CKjclE1Wi2EH2EDz5LRcHcKbCIzqGyg==",
      "dev": true,
      "requires": {
        "isexe": "2.0.0"
      }
    },
    "widest-line": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/widest-line/-/widest-line-1.0.0.tgz",
      "integrity": "sha1-DAnIXCqUaD0Nfq+O4JfVZL8OEFw=",
      "dev": true,
      "requires": {
        "string-width": "1.0.2"
      },
      "dependencies": {
        "ansi-regex": {
          "version": "2.1.1",
          "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
          "integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8=",
          "dev": true
        },
        "is-fullwidth-code-point": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz",
          "integrity": "sha1-754xOG8DGn8NZDr4L95QxFfvAMs=",
          "dev": true,
          "requires": {
            "number-is-nan": "1.0.1"
          }
        },
        "string-width": {
          "version": "1.0.2",
          "resolved": "https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz",
          "integrity": "sha1-EYvfW4zcUaKn5w0hHgfisLmxB9M=",
          "dev": true,
          "requires": {
            "code-point-at": "1.1.0",
            "is-fullwidth-code-point": "1.0.0",
            "strip-ansi": "3.0.1"
          }
        },
        "strip-ansi": {
          "version": "3.0.1",
          "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz",
          "integrity": "sha1-ajhfuIU9lS1f8F0Oiq+UJ43GPc8=",
          "dev": true,
          "requires": {
            "ansi-regex": "2.1.1"
          }
        }
      }
    },
    "write-file-atomic": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-2.3.0.tgz",
      "integrity": "sha512-xuPeK4OdjWqtfi59ylvVL0Yn35SF3zgcAcv7rBPFHVaEapaDr4GdGgm3j7ckTwH9wHL7fGmgfAnb0+THrHb8tA==",
      "dev": true,
      "requires": {
        "graceful-fs": "4.1.11",
        "imurmurhash": "0.1.4",
        "signal-exit": "3.0.2"
      }
    },
    "ws": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/ws/-/ws-3.3.2.tgz",
      "integrity": "sha512-t+WGpsNxhMR4v6EClXS8r8km5ZljKJzyGhJf7goJz9k5Ye3+b5Bvno5rjqPuIBn5mnn5GBb7o8IrIWHxX1qOLQ==",
      "requires": {
        "async-limiter": "1.0.0",
        "safe-buffer": "5.1.1",
        "ultron": "1.1.1"
      }
    },
    "xdg-basedir": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/xdg-basedir/-/xdg-basedir-3.0.0.tgz",
      "integrity": "sha1-SWsswQnsqNus/i3HK2A8F8WHCtQ=",
      "dev": true
    },
    "yallist": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz",
      "integrity": "sha1-HBH5IY8HYImkfdUS+TxmmaaoHVI=",
      "dev": true
    }
  }
}






