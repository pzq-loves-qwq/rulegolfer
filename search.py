from rule import Rule, trans
from spaceship import Spaceship, Failure, evaluate
import os
import re
import random

# Config variables
speeds = [(2, 1, 8), (3, 1, 7), (4, 1, 7), (5, 1, 7)]
forbidden_trans = set(['B0', 'B1c', 'B1e', 'B2a'])
qfind_path = '~/life/qfind/qfind'

def qfind(rule, p, y, w, sym):
    os.system('%s -r %s -p %i -y %i -w %i -s %s -f 1 -a -t 8 > .tmp_out 2>/dev/null' % (qfind_path, str(rule), p, y, w, sym))
    with open('.tmp_out', 'r') as f:
        s = f.read()
        match = re.search('y = (\\d+)', s)
        if match:
            return Spaceship(p, w, int(match[1]))

def find_spaceship(rule, p, y, maxw):
    for w in range(2, maxw + 1):
        for sym in 'eog':
            res = qfind(rule, p, y, w, sym)
            if res:
                return res
    with open('.tmp_out', 'r') as f:
        s = f.read()
        match = re.search('Maximum depth reached: (\\d+)', s)
        return Failure(int(match[1]))

def rule_eval(rule, high_score):
    ret = 0.0
    for (p, y, maxw) in speeds:
        ret += evaluate(find_spaceship(rule, p, y, maxw))
        if ret >= high_score:
            return ret
    return ret

def rand_rule():
    rule = Rule()
    for tran in trans:
        if tran not in forbidden_trans:
            if random.random() <= 0.3:
                rule.toggle(tran)
    return rule

def init_rule():
    s = input()
    if s.startswith('B'):
        return Rule(s)
    ret = Rule()
    high_score = 1e1000

    candidates = 5
    print('Choosing a good initial rule in %i candidates...' % candidates)
    for i in range(candidates):
        rule = rand_rule()
        score = rule_eval(rule, high_score)
        if score < high_score:
            ret = rule
            high_score = score
    return ret

def golf():
    rule = init_rule()
    high_score = rule_eval(rule, float('inf'))
    print('New high score: %f (%s)' % (high_score, str(rule)))

    while True:
        old_high_score = high_score

        for tran in trans:
            if tran not in forbidden_trans:
                rule.toggle(tran)
                score = rule_eval(rule, high_score)
                if score < high_score:
                    print('New high score: %f (%s)' % (high_score, str(rule)))
                    high_score = score
                rule.toggle(tran)

        if high_score == old_high_score:
            print('Local minima reached. ')
            print('Trying to golf out of it...')
            for tran in trans:
                if tran not in forbidden_trans:
                    if random.random() <= 0.1:
                        rule.toggle(tran)
            high_score = rule_eval(rule, float('inf'))

if __name__ == '__main__':
    golf()
