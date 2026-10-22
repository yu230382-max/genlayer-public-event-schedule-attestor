from pathlib import Path

def test_contract_shape():
    text = (Path(__file__).parents[2] / 'contracts' / 'event_schedule_attestor.py').read_text(encoding='utf-8')
    assert 'gl.nondet.web.get' in text
    assert 'gl.nondet.exec_prompt' in text
    assert 'gl.vm.run_nondet_unsafe' in text
    assert '公开活动日程' in text
