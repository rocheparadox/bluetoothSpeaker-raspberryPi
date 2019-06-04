echo "Pairing..."
expect pair_bluetooth_device.expect > expect_script.log

sleep 2

echo "Trusting and connecting.."
device_mac_address=$(cat expect_script.log | grep -Pom 1 "(?<=Device ).*(?= UUID)")
echo mac address is $device_mac_address
expect trust_and_connect.expect $device_mac_address

rm expect_script.log
