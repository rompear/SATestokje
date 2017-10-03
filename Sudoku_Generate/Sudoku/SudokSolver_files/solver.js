function NotEqual(aa, ba) {
    this._leftParm = aa;
    this._rightParm = ba;
}
NotEqual.prototype.getParameters = function() {
    return [this._leftParm, this._rightParm];
};
NotEqual.prototype.evaluate = function(ca) {
    return ca[this._leftParm] != ca[this._rightParm];
};

function Parameter(da, ea) {
    this._name = da;
    this._values = ea;
}
Parameter.prototype.getName = function() {
    return this._name;
};
Parameter.prototype.getValues = function() {
    return this._values;
};

function Constraint(fa, ga) {
    this._name = fa;
    this._expression = ga;
}
Constraint.prototype.getName = function() {
    return this._name;
};
Constraint.prototype.getParameters = function() {
    return this._expression.getParameters();
};
Constraint.prototype.isValid = function(ha) {
    return this._expression.evaluate(ha);
};

function Values() {}

function FirstSolutionObserver() {
    this._solutionFound = false;
}
FirstSolutionObserver.prototype.addSolution = function(ia) {
    this._solutionFound = true;
    this._solution = {};
    for (var i in ia) {
        this._solution[i] = ia[i];
    }
    return false;
};
FirstSolutionObserver.prototype.getSolutionFound = function() {
    return this._solutionFound;
};
FirstSolutionObserver.prototype.getSolution = function() {
    return this._solution;
};

function UniqueSolutionObserver() {
    this._numberOfSolutionsFound = 0;
}
UniqueSolutionObserver.prototype.addSolution = function(ja) {
    if (++this._numberOfSolutionsFound == 1) {
        this._solution = {};
        for (var i in ja) {
            this._solution[i] = ja[i];
        }
        return true;
    } else {
        return false;
    }
};
UniqueSolutionObserver.prototype.getNumberOfSolutionsFound = function() {
    return this._numberOfSolutionsFound;
};
UniqueSolutionObserver.prototype.getSolution = function() {
    return this._solution;
};

function ProgramStepIterate(ka, la, ma, na) {
    this._backtraceStep = ka;
    this._nextStep = la;
    this._parm = ma;
    this._values = na;
    this._currentValue = -1;
}
ProgramStepIterate.prototype.execute = function(oa, pa) {
    if (oa == INIT) {
        this._currentValue = 0;
        pa[this._parm] = this._values[this._currentValue];
        return this._nextStep;
    } else {
        if (++this._currentValue != this._values.length) {
            pa[this._parm] = this._values[this._currentValue];
            return this._nextStep;
        } else {
            return this._backtraceStep;
        }
    }
};

function ProgramStepFinish(qa, ra, sa) {
    this._backtraceStep = qa;
    this._nextStep = ra;
    this._solution = sa;
}
ProgramStepFinish.prototype.execute = function(ta, ua) {
    if (this._solution.addSolution(ua)) {
        return this._backtraceStep;
    } else {
        return this._nextStep;
    }
};

function ProgramStepSetValue(va, wa, xa) {
    this._parameter = wa;
    this._nextStep = va;
    this._value = xa;
}
ProgramStepSetValue.prototype.execute = function(ya, za) {
    za[this._parameter] = this._value;
    return this._nextStep;
};

function ProgramStepValidateExpression(Aa, Ba, Ca) {
    this._backtraceStep = Aa;
    this._nextStep = Ba;
    this._constraint = Ca;
}
ProgramStepValidateExpression.prototype.execute = function(Da, Ea) {
    if (this._constraint.isValid(Ea)) {
        return this._nextStep;
    } else {
        return this._backtraceStep;
    }
};

function updateMaps(Fa, Ga, Ha, Ia) {
    $.each(Fa[Ia], function(Ja, Ka) {
        var La = Ga[Ka.getName()].length;
        $.each(Ha[La], function(Ma, Na) {
            if (Ka.getName() == Na.getName()) {
                Ha[La].splice(Ma, 1);
                return false;
            }
        });
        var Oa = Ga[Ka.getName()];
        $.each(Oa, function(Pa, Qa) {
            if (Ia == Qa) {
                Oa.splice(Pa, 1);
                return false;
            }
        });
        if (Ha[--La] == null) {
            Ha[La] = [];
        }
        Ha[La].push(Ka);
    });
}

function getNextParameter(Ra, Sa, Ta) {
    var Ua = 1;
    while (Ra[Ua] == undefined) {
        ++Ua;
    }
    var Va = {};
    $.each(Ra[Ua], function(Wa, Xa) {
        $.each(Sa[Xa.getName()], function(Wa, Ya) {
            if (!(Ya in Va)) {
                Va[Ya] = 0;
            }
            Va[Ya]++;
        });
    });
    var Za = "";
    $.each(Va, function($a, ab) {
        if ((Za == "") || (ab > Va[Za])) {
            Za = $a;
        }
    });
    return Za;
}

function createProgram(bb, cb, db, eb) {
    var fb = [];
    var gb = {};
    $.each(bb, function(hb, ib) {
        gb[ib.getName()] = [];
    });
    var jb = {};
    var kb = [];
    $.each(cb, function(lb, mb) {
        var nb = mb.getParameters();
        jb[lb] = nb;
        if (kb[nb.length] == null) {
            kb[nb.length] = [];
        }
        kb[nb.length].push(mb);
        $.each(nb, function(ob, pb) {
            gb[pb].push(mb);
        });
    });
    var qb = -1;
    var rb = 0;
    if (db.length != 0) {
        $.each(db, function(sb, tb) {
            fb.push(new ProgramStepSetValue(++rb, sb, tb));
            updateMaps(gb, jb, kb, sb);
            if (kb[0] != null) {
                $.each(kb[0], function(ub, vb) {
                    fb.push(new ProgramStepValidateExpression(qb, ++rb, vb));
                    delete jb[vb.getName()];
                });
                kb[0] = [];
            }
        });
    }
    while (Object.keys(jb).length != 0) {
        var wb = getNextParameter(kb, jb, gb);
        fb.push(new ProgramStepIterate(qb, ++rb, wb, bb[wb].getValues()));
        qb = rb - 1;
        updateMaps(gb, jb, kb, wb);
        if (kb[0] != null) {
            $.each(kb[0], function(xb, yb) {
                fb.push(new ProgramStepValidateExpression(qb, ++rb, yb));
                delete jb[yb.getName()];
            });
            kb[0] = [];
        }
    }
    fb.push(new ProgramStepFinish(qb, ++rb, eb));
    return fb;
}
var INIT = 1;
var INCREMENT = 2;

function executeProgram(zb) {
    var Ab = 0;
    var Bb = {};
    var Cb = INIT;
    while (Ab >= 0 && Ab < zb.length) {
        var Db = zb[Ab].execute(Cb, Bb);
        if (Db > Ab) {
            Cb = INIT;
        } else {
            Cb = INCREMENT;
        }
        Ab = Db;
    }
}

function solve(Eb, Fb, Gb, Hb) {
    var Ib = createProgram(Eb, Fb, Gb, Hb);
    executeProgram(Ib);
}
var model = {
    values: {},
    observers: [],
    setValue: function(Jb, Kb, Lb, Mb) {
        this.values["val" + Jb + "_" + Kb] = Lb;
        this.values["lock" + Jb + "_" + Kb] = Mb;
        for (var Nb in this.observers) {
            this.observers[Nb](Jb, Kb, Lb, Mb);
        }
    },
    getState: function() {
        return this.values;
    },
    setState: function(Ob) {
        var Pb = this;
        $.each(Ob, function(Qb, Rb) {
            if (Qb.length > 3 && Qb.substring(0, 3) == "val") {
                var Sb = Qb.indexOf("_");
                var Tb = parseInt(Qb.substring(3, Sb), 10);
                var Ub = parseInt(Qb.substring(Sb + 1, Qb.length), 10);
                var Vb = Ob["lock" + Qb.substring(3, Qb.length)];
                Pb.setValue(Tb, Ub, Rb, Vb);
            }
        });
    },
    getValue: function(Wb, Xb) {
        return this.values["val" + Wb + "_" + Xb];
    },
    getLock: function(Yb, Zb) {
        return this.values["lock" + Yb + "_" + Zb];
    },
    addObserver: function($b) {
        this.observers.push($b);
    }
};

function getConstraints() {
    var ac = {};
    loopSudokus(function(bc, cc, dc, ec, fc, gc) {
        var hc, col2;
        var ic, row2;
        var jc;
        var kc;
        var lc;
        var mc;
        var nc;
        var oc;
        var pc;
        for (row = 0; row != dc; ++row) {
            for (hc = 0; hc != ec; ++hc) {
                for (col2 = hc + 1; col2 != ec; ++col2) {
                    mc = bc + row;
                    jc = cc + hc;
                    kc = cc + col2;
                    pc = "C" + mc + "_" + jc + "_" + mc + "_" + kc;
                    ac[pc] = new Constraint(pc, new NotEqual("R" + mc + "C" + jc, "R" + mc + "C" + kc));
                }
            }
        }
        for (col = 0; col != ec; ++col) {
            for (ic = 0; ic != dc; ++ic) {
                for (row2 = ic + 1; row2 != dc; ++row2) {
                    lc = cc + col;
                    nc = bc + ic;
                    oc = bc + row2;
                    pc = "C" + nc + "_" + lc + "_" + oc + "_" + lc;
                    ac[pc] = new Constraint(pc, new NotEqual("R" + nc + "C" + lc, "R" + oc + "C" + lc));
                }
            }
        }
        var r1, c1, r2, c2;
        for (row = 0; row != dc; row += fc) {
            for (col = 0; col != ec; col += gc) {
                for (r1 = 0; r1 != fc; ++r1) {
                    for (c1 = 0; c1 != gc; ++c1) {
                        for (r2 = 0; r2 != fc; ++r2) {
                            for (c2 = 0; c2 != gc; ++c2) {
                                if (((r2 > r1) || ((r2 == r1) && (c2 > c1))) && ((r1 != r2) && (c1 != c2))) {
                                    nc = bc + row + r1;
                                    jc = cc + col + c1;
                                    oc = bc + row + r2;
                                    kc = cc + col + c2;
                                    pc = "C" + nc + "_" + jc + "_" + oc + "_" + kc;
                                    ac[pc] = new Constraint(pc, new NotEqual("R" + nc + "C" + jc, "R" + oc + "C" + kc));
                                }
                            }
                        }
                    }
                }
            }
        }
    });
    return ac;
}

function getParameters() {
    var qc = {};
    var rc = [];
    for (var sc = 1; sc != symbols.length; ++sc) {
        rc.push(sc);
    }
    loopSudokus(function(tc, uc, vc, wc, xc, yc) {
        for (row = 0; row != vc; ++row) {
            for (col = 0; col != wc; ++col) {
                var zc = tc + row;
                var Ac = uc + col;
                var Bc = "R" + zc + "C" + Ac;
                qc[Bc] = new Parameter(Bc, rc);
            }
        }
    });
    return qc;
}