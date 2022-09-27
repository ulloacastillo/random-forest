use rand::prelude::*;
use std::fs::File;
use std::io::Read;
use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};

mod dtree;
mod utils;
mod random_forest;

#[derive(Debug, Deserialize, Serialize)]
struct Data {
    n_trees: usize,
    min_samples_split: usize,
    max_depth: usize,
    n_feats: usize,
    seed: u64,
}

#[wasm_bindgen]
pub fn main(json: &JsValue, train_dataset: &JsValue, train_labels: &JsValue, task_type: &JsValue)  -> JsValue {
    let task: String = task_type.into_serde().unwrap();

    if "predict".to_string().eq(&task) {
        let mut rf: random_forest::RandomForest = json.into_serde().unwrap();
        let x_test: Vec<Vec<f32>> = train_dataset.into_serde().unwrap();
        
        let y_pred = rf.predict(&x_test);
        JsValue::from_serde(&y_pred).unwrap()
    }

    else {
        let params: Data = json.into_serde().unwrap();

        let mut x: Vec<Vec<f32>> = train_dataset.into_serde().unwrap();
        let mut y: Vec<String> = train_labels.into_serde().unwrap();

        let seed: u64 = params.seed;

        let (x_train, y_train, _x_test, _y_test) = utils::split_dataset(&mut x, &mut y, 0.8);

        // Parameters: n_trees, min_samples_split, max_depth, n_feats
        let mut rf = random_forest::RandomForest::new(100, 3, 3, 4, seed);
        
        rf.fit(&x_train, &y_train);

        let y_pred = rf.predict(&x_train);
        
        let percent = random_forest::accuracy(&y_pred, &y_train);
        
        JsValue::from_serde(&percent).unwrap()
    }


}