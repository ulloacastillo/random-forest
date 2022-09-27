<div align="center">

  <h1>Motivus Random Forest <code>wasm-pack</code></h1>

  <strong>A Random Forest Classifier powered by <a href="https://motivus.cl/">Motivus Waterbear Cluster</a> processing  power.</strong>

  <h3>
    <a href="https://motivus.cl/documentation/">Learn more</a>
    <span> | </span>
    <a href="https://discord.gg/t8f5xNhTJW">Join us on Discord</a>
  </h3>
</div>

## 🚴 Usage

### 🐑 Use `cargo generate` to Clone this Template

[Learn more about `cargo generate` here.](https://github.com/ashleygwilliams/cargo-generate)

```
cargo generate --git https://github.com/m0tivus/wasm-pack-template.git --name my-project
cd my-project
```




## 🛠️ Development Environment Requirements
* Docker
   * Your user must belong to the `docker` group.
* Python = 3.7 | 3.8 | 3.9
   * We recommend using a `conda` environment.
* [*Motivus CLI tool* and *Motivus Client library*](https://pypi.org/project/motivus/): `$ pip install motivus`

### 🛠️ Build with `motivus build`

```
$ motivus build
```
### 🔬 Driver usage

class RandomForest.RandomForestClassifier(model_path=None, n_estimators=100, min_samples_split=2, max_depth=3, n_features=4, seed=41)

Parameters

| Name  | Description  |
|---|---|
| model_path: string, default=None  | The path of the pickle file that contains a pre-trained tree. Use it in case you want to predict new samples  |
| n_estimators: int, default=100  | The number of trees in the forest  |
| min_samples_split: int, default=2  | The minimum number of samples required to split an internal node  |
| max_depth: int, default=3  |  The maximum depth of the tree |
| n_features: int, default=4  | The number of features to consider when looking for the best split  |
| seed: int, default=41  | Controls the randomness of the bootstrapping of the samples used when building trees and the sampling of the features to consider when looking for the best split at each node.  |

Methods

| Name  | Description  |
| `fit(x, y)` | Train (build) a RandomForestClassifier from training set(x, y) where `x` are the samples and `y`. |
| `predict(x)` | Return the label (class) of the predictions did for each sample of the set x. |

Driver Example (python3)

```
from RandomForest import RandomForestClassifier

file_name = "/Users/ulloacastillo/Desktop/rust/motivus-random-forest/random_forest.pickle"

x = [
      [5.1, 3.5, 1.4, 0.2],
      [4.9, 3, 1.4, 0.2],
      [4.7, 3.2, 1.3, 0.2],
      [4.6, 3.1, 1.5, 0.2],
      [5, 3.6, 1.4, 0.2],
      [5.4, 3.9, 1.7, 0.4],
      [4.6, 3.4, 1.4, 0.3],
      [5, 3.4, 1.5, 0.2],
      [4.4, 2.9, 1.4, 0.2]
    ]
y = ["setosa", "versicolor", "virginica", "setosa", "setosa", "virginica", "setosa", "versicolor", "setosa"]

x_test = [[6.8, 2.8, 4.8, 1.4], [6.7, 3, 5, 1.7], [6, 2.9, 4.5, 1.5], [5.7, 2.6, 3.5, 1], [5.5, 2.4, 3.8, 1.1], [5.5, 2.4, 3.7, 1]]

rf = RandomForestClassifier(n_estimators=100, min_samples_split=2, max_depth=3, n_features=4, seed=41)


rf.fit(x, y)
rf.predict(x_test)

```


### 🔬 Test locally with `motivus loopback`

```
$ motivus loopback
```
```
$ WEBSOCKET_URI=ws://localhost:7070/client_socket/websocket python driver.py
```

### 🎁 Publish to Motivus Marketplace with `motivus push`

```
$ motivus push
```

## 🔋 Batteries Included

* [`wasm-bindgen`](https://github.com/rustwasm/wasm-bindgen) for communicating
  between WebAssembly and JavaScript.
* [`console_error_panic_hook`](https://github.com/rustwasm/console_error_panic_hook)
  for logging panic messages to the developer console.
* [`wee_alloc`](https://github.com/rustwasm/wee_alloc), an allocator optimized
  for small code size.
