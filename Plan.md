# Plan: 시나리오 1 — 모든 거터볼 (score 0)

## 목표 (Goal)

`Game` 클래스에 `roll(pins)`와 `score()` 메서드를 도입한다.
20번의 롤을 모두 거터볼(0핀)로 던졌을 때, `score()`는 `0`을 반환해야 한다.

이번 사이클에서는 **오직 이 시나리오만** 다룬다. 스페어, 스트라이크, 10프레임 보너스 로직은
이후 사이클에서 각각 별도의 Plan으로 다룬다.

## 접근 방식 (Approach)

- `src/game.py`에 `Game` 클래스를 새로 만든다.
- `roll(pins)`는 굴린 핀 수를 내부 리스트에 저장하는 정도로 최소 구현한다.
- `score()`는 저장된 롤들의 합을 반환하는 정도로 최소 구현한다.
  (모든 롤이 0이므로 합계 로직은 이 시나리오를 통과시키는 가장 단순한 코드가 된다.
  스페어/스트라이크 보너스 계산은 이후 사이클에서 테스트가 요구할 때 추가한다.)

## 작성할 실패 테스트 (Failing test to write)

`tests/test_game.py`

```python
from src.game import Game

def test_gutter_game_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0
```

## 예상되는 RED 실패 사유

- `src/game.py` 및 `Game` 클래스가 아직 존재하지 않으므로 `ModuleNotFoundError` 또는
  `ImportError`로 실패해야 한다 (오타가 아니라 구현 부재로 인한 실패).

## 범위 밖 (Out of scope for this cycle)

- 1핀 롤 시나리오
- 스페어 처리
- 스트라이크 처리
- 10프레임 보너스 롤
- 퍼펙트 게임
