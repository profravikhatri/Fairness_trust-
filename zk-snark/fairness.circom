
pragma circom 2.0.0;
template FairnessCheck(){
 signal input r_pre;
 signal input r_ideal;
 signal input lambda;
 signal output r_post;
 r_post <== r_pre + lambda*(r_ideal-r_pre);
}
component main = FairnessCheck();
