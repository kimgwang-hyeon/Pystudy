import numpy as np

def solution(m, n, h, w, drops):
    R, C = m - h + 1, n - w + 1          # 선인장 좌상단 후보 격자 크기
    d = np.asarray(drops, dtype=np.int64)
    r, c = d[:, 0], d[:, 1]
    # 빗방울 (r,c)가 적시는 "좌상단 후보" 직사각형 [r1..r2] x [c1..c2]
    r1 = np.maximum(0, r - h + 1)
    c1 = np.maximum(0, c - w + 1)
    r2 = np.minimum(R - 1, r)
    c2 = np.minimum(C - 1, c)

    W = C + 1
    size = (R + 1) * W
    i00 = r1 * W + c1
    i01 = r1 * W + (c2 + 1)
    i10 = (r2 + 1) * W + c1
    i11 = (r2 + 1) * W + (c2 + 1)

    def coverage(t):  # 앞 t개의 drop이 만드는 커버 횟수 격자 (R x C)
        diff = (np.bincount(i00[:t], minlength=size)
                - np.bincount(i01[:t], minlength=size)
                - np.bincount(i10[:t], minlength=size)
                + np.bincount(i11[:t], minlength=size)).reshape(R + 1, W)
        return diff.cumsum(0).cumsum(1)[:R, :C]

    K = len(drops)
    lo, hi = 1, K + 1   # lo = "앞 t개가 전부 덮는" 최소 t, 없으면 K+1
    while lo < hi:
        mid = (lo + hi) // 2
        if (coverage(mid) > 0).all():
            hi = mid
        else:
            lo = mid + 1

    cov = coverage(lo - 1)               # 그 직전까지 안 젖은 칸들이 최적 후보
    idx = int(np.argmin(cov.reshape(-1) > 0))  # row-major 첫 0 = 가장 위, 가장 왼쪽
    return [idx // C, idx % C]
