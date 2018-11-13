#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;


struct point {
  double x;
  double y;
};


struct triangle {
  point a;
  point b;
  point c;
};


double yIntercept(point p1, point p2) {
  double slope = (p2.y - p1.y) / (p2.x - p1.x);
  double yInt = p1.y - (slope * p1.x);
  return yInt;
}


bool containsOrigin(triangle *t) {
  point p;
  point other1, other2;

  if ((t->a.x * t->b.x) > 0) {
    p = t->c;
    other1 = t->a;
    other2 = t->b;
  }
  else if ((t->a.x * t->c.x) > 0) {
    p = t->b;
    other1 = t->a;
    other2 = t->c;
  }
  else {
    p = t->a;
    other1 = t->b;
    other2 = t->c;
  }

  double yInt1 = yIntercept(p, other1);
  double yInt2 = yIntercept(p, other2);

  if ((yInt1 * yInt2) < 0) {
    return true;
  }
  return false;
}


int main(void) {
  vector<triangle*> triangles;

  ifstream tri;
  tri.open ("p102_triangles.txt");
  
  std::string line;
  while (std::getline(tri, line)) {
    std::istringstream iss(line);

    triangle * t1 = new triangle;

    iss >> t1->a.x;
    iss.get();
    iss >> t1->a.y;
    iss.get();
    iss >> t1->b.x;
    iss.get();
    iss >> t1->b.y;
    iss.get();
    iss >> t1->c.x;
    iss.get();
    iss >> t1->c.y;
    iss.get();

    triangles.push_back(t1);
  }
  tri.close();

  int contains = 0;
  int numTriangles = triangles.size();
  for (int i = 0; i < numTriangles; ++i) {
    cout << i << endl;
    int numRightOfOrigin = 0;
    triangle *t = triangles[i];
    if (t->a.x > 0) ++numRightOfOrigin;
    if (t->b.x > 0) ++numRightOfOrigin;
    if (t->c.x > 0) ++numRightOfOrigin;
    if ((numRightOfOrigin == 1) || (numRightOfOrigin == 2)) {
      if (containsOrigin(t)) {
        contains++;
      }
    }
  }

  cout << contains << endl;

  for (int i = 0; i < numTriangles; ++i) {
    delete triangles[i];
  }
}
