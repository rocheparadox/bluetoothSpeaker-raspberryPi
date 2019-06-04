cd $(dirname $0)
echo "Pairing..."
expect pair_bluetooth_device.expect > expect_script.log
chmod 777 expect_script.log
sleep 2

echo "Trusting and connecting.."
device_mac_address=$(cat expect_script.log | grep -Pom 1 "(?<=Device ).*(?= Connected)")
echo mac address is $device_mac_address
if [[ ! -z $device_mac_address ]] ; then
	expect trust_and_connect.expect $device_mac_address
else
	echo "No device connected"
fi
rm expect_script.log
