int gcd(int a, int b) {
  int v0 = a, v1 = b, v2 = a % b;
  while (v2 != 0) {
    v0 = v1;
    v1 = v2;
    v2 = v0 % v1;
  };
  return v1;
}

int lcm(int a, int b) {
  return a * b / gcd(a, b);
}

